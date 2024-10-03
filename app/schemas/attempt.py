from pydantic import BaseModel

class AttemptCreate(BaseModel):
    user_id: int
    problem_id: int
    status: str
