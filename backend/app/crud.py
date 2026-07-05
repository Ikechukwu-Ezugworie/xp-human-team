from sqlalchemy.orm import Session
from app import models
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_user(db: Session, username: str, password: str) -> models.User:
    hashed = hash_password(password)
    user = models.User(username=username, password_hash=hashed)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def create_room(
    db: Session, name: str, description: str, created_by: int
) -> models.Room:
    room = models.Room(name=name, description=description, created_by=created_by)
    db.add(room)
    db.commit()
    db.refresh(room)
    return room


def get_rooms(db: Session):
    return db.query(models.Room).all()


def get_room_by_id(db: Session, room_id: int):
    return db.query(models.Room).filter(models.Room.id == room_id).first()


def join_room(db: Session, room_id: int, user_id: int):
    room = get_room_by_id(db, room_id)
    user = get_user_by_id(db, user_id)
    if room and user and user not in room.members:
        room.members.append(user)
        db.commit()


def send_message(
    db: Session, room_id: int, author_id: int, content: str
) -> models.Message:
    message = models.Message(room_id=room_id, author_id=author_id, content=content)
    db.add(message)
    db.commit()
    db.refresh(message)
    return message


def get_room_messages(db: Session, room_id: int, limit: int = 50, offset: int = 0):
    return (
        db.query(models.Message)
        .filter(models.Message.room_id == room_id)
        .order_by(models.Message.created_at.desc())
        .offset(offset)
        .limit(limit)
        .all()
    )
