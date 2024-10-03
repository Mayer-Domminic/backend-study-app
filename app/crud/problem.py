from sqlalchemy.orm import Session
from app.models.problem import Problem

def create_problem(db: Session, title: str, difficulty: str, topic: str, url: str):
    db_problem = Problem(title=title, difficulty=difficulty, topic=topic, url=url)
    db.add(db_problem)
    db.commit()
    db.refresh(db_problem)
    return db_problem

def get_problems(db: Session):
    return db.query(Problem).all()
