from fastapi import WebSocket
from typing import Dict, List, Tuple


class ConnectionManager:
    """Tracks WebSocket connections per room, with the username behind each socket."""

    def __init__(self):
        self.rooms: Dict[int, List[Tuple[WebSocket, str]]] = {}

    async def connect(self, room_id: int, websocket: WebSocket, username: str):
        await websocket.accept()
        self.rooms.setdefault(room_id, []).append((websocket, username))
        await self.broadcast_presence(room_id)

    async def disconnect(self, room_id: int, websocket: WebSocket):
        connections = self.rooms.get(room_id, [])
        self.rooms[room_id] = [(ws, name) for ws, name in connections if ws is not websocket]
        await self.broadcast_presence(room_id)

    def online_users(self, room_id: int) -> List[str]:
        seen = set()
        users = []
        for _, name in self.rooms.get(room_id, []):
            if name not in seen:
                seen.add(name)
                users.append(name)
        return users

    async def broadcast_presence(self, room_id: int):
        await self.broadcast(room_id, {"type": "presence", "users": self.online_users(room_id)})

    async def broadcast(self, room_id: int, data: dict):
        for ws, _ in list(self.rooms.get(room_id, [])):
            try:
                await ws.send_json(data)
            except Exception:
                pass


manager = ConnectionManager()
