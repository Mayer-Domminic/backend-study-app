from sqlalchemy.exc import SQLAlchemyError
from .db import Base, engine
from app.models import user, item, tag, attempt, settings

def init_db():
    """
    Initialize the database by creating all tables defined in the models.
    """
    try:
        # Create all tables in the database
        Base.metadata.create_all(bind=engine)
        print("Database initialized successfully.")
    except SQLAlchemyError as e:
        print(f"Error initializing database: {e}")

if __name__ == "__main__":
    init_db()