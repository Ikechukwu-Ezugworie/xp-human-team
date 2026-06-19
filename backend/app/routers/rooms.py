from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import create_room, get_rooms, get_room_by_id, join_room
from app.schemas import RoomCreate, Room
from app.main import get_db

router = APIRouter(prefix="/api/rooms", tags=["rooms"])

@router.post("/", response_model=Room)
async def create_room_endpoint(room: RoomCreate, db: Session = Depends(get_db)):
    existing = db.query(db.Model).filter_by(name=room.name).first()
    if existing:
        raise HTTPException(status_code=400, detail="Room name already exists")
    new_room = create_room(db, room.name, room.description or "", user_id=1)
    return new_room

@router.get("/", response_model=list[Room])
async def list_rooms(db: Session = Depends(get_db)):
    return get_rooms(db)

@router.get("/{room_id}", response_model=Room)
async def get_room(room_id: int, db: Session = Depends(get_db)):
    room = get_room_by_id(db, room_id)
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    return room

@router.post("/{room_id}/join")
async def join_room_endpoint(room_id: int, db: Session = Depends(get_db)):
    room = get_room_by_id(db, room_id)
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    join_room(db, room_id, user_id=1)
    return {"detail": "Joined room"}
