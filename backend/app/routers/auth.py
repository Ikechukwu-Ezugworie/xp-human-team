from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import create_user, get_user_by_username, verify_password
from app.schemas import UserRegister, UserLogin, TokenResponse
from app.database import get_db
from app.security import create_access_token

router = APIRouter(prefix="/api/auth", tags=["auth"])


@router.post("/register", response_model=TokenResponse)
async def register(user_data: UserRegister, db: Session = Depends(get_db)):
    existing = get_user_by_username(db, user_data.username)
    if existing:
        raise HTTPException(status_code=400, detail="Username already registered")
    user = create_user(db, user_data.username, user_data.password)
    token = create_access_token(user.id)
    return {"access_token": token, "token_type": "bearer"}


@router.post("/login", response_model=TokenResponse)
async def login(user_data: UserLogin, db: Session = Depends(get_db)):
    user = get_user_by_username(db, user_data.username)
    if not user or not verify_password(user_data.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token(user.id)
    return {"access_token": token, "token_type": "bearer"}


@router.post("/logout")
async def logout():
    return {"detail": "Logged out"}
