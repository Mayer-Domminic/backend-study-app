from pydantic import BaseModel

class User(BaseModel):
    id: int
    username: str
    email: str
    password_hash: str

class Document(BaseModel):
    id: int
    user_id: int
    class_id: int
    document_data: dict

class Flashcard(BaseModel):
    id: int
    user_id: int
    class_id: int
    flashcard_data: dict

class Class(BaseModel):
    id: int
    user_id: int
    name: str
