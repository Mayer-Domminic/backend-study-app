from pydantic import BaseModel
from datetime import datetime

class AttemptCreate(BaseModel):
    user_id: int
    item_id: int
    time_taken: int
    success: bool
    date: datetime.date
    sol_used: bool