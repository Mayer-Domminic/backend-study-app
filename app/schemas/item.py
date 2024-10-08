from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ItemBase(BaseModel):
    user_id: int
    tag_id: int
    name: str
    difficulty: Optional[str] = None
    number: Optional[int] = None
    src: Optional[str] = None

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    item_id: int
    created_at: datetime

    class Config:
        from_attributes = True