from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import attempt
from app.database.db import get_db
from app.schemas.attempt import AttemptCreate

router = APIRouter()

@router.post("/attempts/")
def create_attempt(attempt_data: AttemptCreate, db: Session = Depends(get_db)):
    return attempt.create_attempt(db, attempt_data.user_id, attempt_data.problem_id, attempt_data.status)

@router.get("/attempts/user/{user_id}")
def get_attempts_by_user(user_id: int, db: Session = Depends(get_db)):
    return attempt.get_attempts_by_user(db, user_id)

@router.get("/attempts/problem/{problem_id}")
def get_attempts_by_problem(problem_id: int, db: Session = Depends(get_db)):
    return attempt.get_attempts_by_problem(db, problem_id)

@router.get("/attempts/{attempt_id}")
def get_attempt(attempt_id: int, db: Session = Depends(get_db)):
    db_attempt = attempt.get_attempt(db, attempt_id)
    if not db_attempt:
        raise HTTPException(status_code=404, detail="Attempt not found")
    return db_attempt
