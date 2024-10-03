from pydantic import BaseModel

class ProblemCreate(BaseModel):
    title: str
    difficulty: str
    topic: str
    url: str
