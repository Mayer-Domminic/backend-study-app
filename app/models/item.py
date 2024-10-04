from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.sql import func
from app.database.db import Base

class Item(Base):
    __tablename__ = "Items"
    item_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('Users.user_id'), nullable=False)
    tag = Column(String(20), nullable=True)
    name = Column(String(255), nullable=False)
    difficulty = Column(String(10), nullable=True)
    number = Column(Integer, nullable=True)
    src = Column(String(20), nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
