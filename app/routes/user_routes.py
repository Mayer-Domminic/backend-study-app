from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import user
from app.database.db import get_db

router = APIRouter()

@router.post("/users/")
def create_user(username: str, email: str, password_hash: str, db: Session = Depends(get_db)):
    existing_user = user.get_user_by_username_or_email(db, username, email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username or email already registered")
    return user.create_user(db, username, email, password_hash)
