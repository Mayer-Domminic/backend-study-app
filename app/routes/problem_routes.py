from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.crud import problem
from app.database.db import get_db

router = APIRouter()

@router.get("/problems/")
def get_problems(db: Session = Depends(get_db)):
    return problem.get_problems(db)

@router.post("/problems/")
def create_problem(title: str, difficulty: str, topic: str, url: str, db: Session = Depends(get_db)):
    return problem.create_problem(db, title, difficulty, topic, url)
