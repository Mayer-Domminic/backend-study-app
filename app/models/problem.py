from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.sql import func
from app.database.db import Base

class Problem(Base):
    __tablename__ = "Problems"
    problem_id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    difficulty = Column(String(10), nullable=False)
    topic = Column(String(100))
    url = Column(String(255))
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
