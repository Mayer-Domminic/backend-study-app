from sqlalchemy.orm import Session
from app.models.user import User

def create_user(db: Session, username: str, email: str, password_hash: str):
    db_user = User(username=username, email=email, password_hash=password_hash)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.user_id == user_id).first()

def get_user_by_username_or_email(db: Session, username: str, email: str):
    return db.query(User).filter((User.username == username) | (User.email == email)).first()