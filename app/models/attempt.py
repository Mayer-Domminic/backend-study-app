from sqlalchemy import Column, Integer, Boolean, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Attempt(Base):
    __tablename__ = 'attempts'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    item_id = Column(Integer, ForeignKey('items.id'), nullable=False)
    time_taken = Column(Integer, nullable=False)
    success = Column(Boolean, nullable=False)
    date = Column(Date, nullable=False)
    sol_used = Column(Boolean, nullable=False)