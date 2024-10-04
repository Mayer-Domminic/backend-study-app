from pydantic import BaseModel
from datetime import date

class AttemptBase(BaseModel):
    user_id: int
    item_id: int
    tag: str
    time_taken: int
    success: bool
    date: date
    sol_used: bool

class AttemptCreate(AttemptBase):
    pass

class Attempt(AttemptBase):
    id: int

    class Config:
        from_attributes = True