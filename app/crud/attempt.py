from sqlalchemy.orm import Session
from app.models.attempt import Attempt

def create_attempt(db: Session, user_id: int, problem_id: int, status: str):
    db_attempt = Attempt(user_id=user_id, problem_id=problem_id, status=status)
    db.add(db_attempt)
    db.commit()
    db.refresh(db_attempt)
    return db_attempt

def get_attempts_by_user(db: Session, user_id: int):
    return db.query(Attempt).filter(Attempt.user_id == user_id).all()

def get_attempts_by_problem(db: Session, problem_id: int):
    return db.query(Attempt).filter(Attempt.problem_id == problem_id).all()

def get_attempt(db: Session, attempt_id: int):
    return db.query(Attempt).filter(Attempt.attempt_id == attempt_id).first()
