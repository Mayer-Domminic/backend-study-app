from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import user
from app.database.db import get_db

router = APIRouter()

@router.post("/users/")
def create_user(username: str, email: str, password_hash: str, db: Session = Depends(get_db)):
    return user.create_user(db, username, email, password_hash)
