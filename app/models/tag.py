from sqlalchemy import Column, Integer, String
from app.database.db import Base

class Tag(Base):
    __tablename__ = 'tags'
    tag_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20), nullable=False)
