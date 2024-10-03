from pydantic import BaseModel

class ItemCreate(BaseModel):
    item_id: int
    tag: str
    difficulty: str
    src: str
    number: int
    name: str

