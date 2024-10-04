from sqlalchemy import Column, Integer, String, ForeignKey
from app.database.db import Base

class Setting(Base):
    __tablename__ = 'Settings'
    settings_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('Users.user_id'), nullable=False)
    grind = Column(Integer, nullable=False)
    problems_per_day = Column(Integer, nullable=False)
    noti_time = Column(Integer, nullable=False)
    days_of_week = Column(String(255), nullable=False)