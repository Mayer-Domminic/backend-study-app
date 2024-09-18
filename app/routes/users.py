from fastapi import APIRouter, Depends, HTTPException, status
from app.auth import create_access_token, get_password_hash
from app.crud import create_user, get_user_by_username
from app.dependencies import get_current_user
from app.database import get_db

router = APIRouter()

@router.post("/register")
def register(username: str, email: str, password: str, db=Depends(get_db)):
    password_hash = get_password_hash(password)
    user_id = create_user(db, username, email, password_hash)
    return {"message": "User created successfully", "user_id": user_id}

@router.post("/login")
def login(username: str, password: str, db=Depends(get_db)):
    user = get_user_by_username(db, username)
    if not user or not verify_password(password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    access_token = create_access_token(data={"sub": username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.delete("/user")
def delete_user(current_user=Depends(get_current_user), db=Depends(get_db)):
    # Implement user deletion logic
    return {"message": "User deleted successfully"}
