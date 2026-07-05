from fastapi import Depends, Header, HTTPException
from sqlalchemy.orm import Session
import jwt
import os
from app.database import get_db

SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")
ALGORITHM = "HS256"


def create_access_token(user_id: int) -> str:
    return jwt.encode({"sub": str(user_id)}, SECRET_KEY, algorithm=ALGORITHM)


def get_current_user(
    authorization: str = Header(default=None), db: Session = Depends(get_db)
):
    from app.crud import get_user_by_id

    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Not authenticated")
    token = authorization.split(" ", 1)[1]
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = int(payload["sub"])
    except (jwt.PyJWTError, KeyError, ValueError):
        raise HTTPException(status_code=401, detail="Invalid token")
    user = get_user_by_id(db, user_id)
    if user is None:
        raise HTTPException(status_code=401, detail="User not found")
    return user
