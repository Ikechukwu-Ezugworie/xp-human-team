from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
import os
from app import models
from app.database import engine
from app.routers import auth, rooms, messages
from app.websocket import manager

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Chat API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("CORS_ORIGINS", "http://localhost:3000").split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(rooms.router)
app.include_router(messages.router)


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.websocket("/ws/{room_id}")
async def websocket_endpoint(
    room_id: int, websocket: WebSocket, username: str = "anonymous"
):
    await manager.connect(room_id, websocket, username)
    try:
        while True:
            # Messages are persisted and broadcast via the REST endpoint;
            # the socket stays open for presence and server pushes.
            await websocket.receive_json()
    except WebSocketDisconnect:
        await manager.disconnect(room_id, websocket)
