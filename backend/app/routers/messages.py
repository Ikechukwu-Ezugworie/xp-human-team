from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models
from app.crud import send_message, get_room_messages, get_room_by_id
from app.schemas import MessageCreate, Message
from app.database import get_db
from app.security import get_current_user
from app.websocket import manager

router = APIRouter(prefix="/api/messages", tags=["messages"])


@router.post("/{room_id}", response_model=Message)
async def create_message(
    room_id: int,
    msg: MessageCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    content = msg.content.strip()
    if not content:
        raise HTTPException(status_code=400, detail="Message cannot be empty")
    if not get_room_by_id(db, room_id):
        raise HTTPException(status_code=404, detail="Room not found")
    message = send_message(db, room_id, author_id=current_user.id, content=content)
    await manager.broadcast(
        room_id,
        {
            "type": "message",
            "message": {
                "id": message.id,
                "room_id": message.room_id,
                "author_id": message.author_id,
                "author_name": current_user.username,
                "content": message.content,
                "created_at": message.created_at.isoformat(),
            },
        },
    )
    return message


@router.get("/{room_id}", response_model=list[Message])
async def get_messages(
    room_id: int,
    skip: int = 0,
    limit: int = 50,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    return get_room_messages(db, room_id, limit=limit, offset=skip)
