from sqlalchemy import Column, Integer, ForeignKey, TIMESTAMP, String
from sqlalchemy.sql import func
from app.database.db import Base

class Attempt(Base):
    __tablename__ = "Attempts"
    attempt_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("Users.user_id"), nullable=False)
    problem_id = Column(Integer, ForeignKey("Problems.problem_id"), nullable=False)
    status = Column(String(50), nullable=False)  # e.g., 'Solved', 'Failed'
    attempt_time = Column(TIMESTAMP(timezone=True), server_default=func.now())
