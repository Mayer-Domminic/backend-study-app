from fastapi import FastAPI
from app.routes import users, documents, flashcards

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(documents.router, prefix="/documents", tags=["documents"])
app.include_router(flashcards.router, prefix="/flashcards", tags=["flashcards"])
