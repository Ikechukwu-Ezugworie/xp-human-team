from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models
from app.crud import create_room, get_rooms, get_room_by_id, join_room
from app.schemas import RoomCreate, Room
from app.database import get_db
from app.security import get_current_user

router = APIRouter(prefix="/api/rooms", tags=["rooms"])


@router.post("/", response_model=Room)
async def create_room_endpoint(
    room: RoomCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    name = room.name.strip()
    if not name:
        raise HTTPException(status_code=400, detail="Room name cannot be empty")
    existing = db.query(models.Room).filter_by(name=name).first()
    if existing:
        raise HTTPException(status_code=400, detail="Room name already exists")
    new_room = create_room(db, name, room.description or "", created_by=current_user.id)
    join_room(db, new_room.id, current_user.id)
    return new_room


@router.get("/", response_model=list[Room])
async def list_rooms(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    return get_rooms(db)


@router.get("/{room_id}", response_model=Room)
async def get_room(
    room_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    room = get_room_by_id(db, room_id)
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    return room


@router.post("/{room_id}/join")
async def join_room_endpoint(
    room_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    room = get_room_by_id(db, room_id)
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    join_room(db, room_id, current_user.id)
    return {"detail": "Joined room"}
