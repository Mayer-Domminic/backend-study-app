from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database.db import get_db
from ..models.attempt import Attempt
from ..schemas.attempt import AttemptCreate, Attempt as AttemptSchema
from ..models.user import User
from ..models.item import Item

router = APIRouter(prefix="/attempts", tags=["attempts"])

@router.post("/", response_model=AttemptSchema)
def create_attempt(attempt: AttemptCreate, db: Session = Depends(get_db)):
    # Check if the user exists
    user = db.query(User).filter(User.user_id == attempt.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Check if the item exists
    item = db.query(Item).filter(Item.item_id == attempt.item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    # Optional: Check if the tag exists
    if attempt.tag:
        tag_exists = db.query(Item).filter(Item.tags == attempt.tag).first()
        if not tag_exists:
            raise HTTPException(status_code=404, detail="Tag not found")

    db_attempt = Attempt(**attempt.dict())
    db.add(db_attempt)
    db.commit()
    db.refresh(db_attempt)
    return db_attempt

@router.get("/{user_id}", response_model=List[AttemptSchema])
def read_attempts(user_id: int, db: Session = Depends(get_db)):
    attempts = db.query(Attempt).filter(Attempt.user_id == user_id).all()
    if not attempts:
        raise HTTPException(status_code=404, detail="Attempts not found")
    return attempts

@router.put("/{attempt_id}", response_model=AttemptSchema)
def update_attempt(attempt_id: int, attempt: AttemptCreate, db: Session = Depends(get_db)):
    db_attempt = db.query(Attempt).filter(Attempt.id == attempt_id).first()
    if not db_attempt:
        raise HTTPException(status_code=404, detail="Attempt not found")
    
    for key, value in attempt.dict().items():
        setattr(db_attempt, key, value)
    
    db.commit()
    db.refresh(db_attempt)
    return db_attempt

@router.delete("/{attempt_id}")
def delete_attempt(attempt_id: int, db: Session = Depends(get_db)):
    db_attempt = db.query(Attempt).filter(Attempt.id == attempt_id).first()
    if not db_attempt:
        raise HTTPException(status_code=404, detail="Attempt not found")
    
    db.delete(db_attempt)
    db.commit()
    return {"message": "Attempt deleted successfully"}
