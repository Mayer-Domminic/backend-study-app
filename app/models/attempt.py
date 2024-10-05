from sqlalchemy import Column, Integer, Boolean, Date, ForeignKey, String
from app.database.db import Base

class Attempt(Base):
    __tablename__ = 'attempts'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    item_id = Column(Integer, ForeignKey('items.item_id'), nullable=False)
    time_taken = Column(Integer, nullable=False)
    success = Column(Boolean, nullable=False)
    date = Column(Date, nullable=False)
    sol_used = Column(Boolean, nullable=False)
