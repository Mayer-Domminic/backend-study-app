from app.models import User
from app.database import get_db

def get_user_by_username(db, username: str):
    with db.cursor() as cur:
        cur.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cur.fetchone()
    return User(**user) if user else None

def create_user(db, username: str, email: str, password_hash: str):
    with db.cursor() as cur:
        cur.execute("""
            INSERT INTO users (username, email, password_hash) 
            VALUES (%s, %s, %s) RETURNING id
        """, (username, email, password_hash))
        user_id = cur.fetchone()[0]
    db.commit()
    return user_id
