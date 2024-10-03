from .db import Base, engine
from app.models import user, problem, user_problem, attempt

def init_db():
    # Ensure all models are created in the database
    Base.metadata.create_all(bind=engine)
