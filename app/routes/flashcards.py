from fastapi import APIRouter, Depends
from app.dependencies import get_current_user

router = APIRouter()

@router.post("/flashcards")
async def create_flashcards(class_id: int, flashcards_data: dict, user: dict = Depends(get_current_user)):
    # Save the flashcards JSON to the database
    return {"message": "Flashcards saved"}
