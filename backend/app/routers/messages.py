from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import send_message, get_room_messages
from app.schemas import MessageCreate, Message
from app.main import get_db

router = APIRouter(prefix="/api/messages", tags=["messages"])

@router.post("/{room_id}", response_model=Message)
async def create_message(room_id: int, msg: MessageCreate, db: Session = Depends(get_db)):
    message = send_message(db, room_id, author_id=1, content=msg.content)
    return message

@router.get("/{room_id}", response_model=list[Message])
async def get_messages(room_id: int, skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    return get_room_messages(db, room_id, limit=limit, offset=skip)
