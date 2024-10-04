from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database.db import get_db
from ..models.settings import Setting
from ..schemas.settings import SettingCreate, Setting as SettingSchema
from ..models.user import User

router = APIRouter(prefix="/settings", tags=["settings"])

@router.post("/", response_model=SettingSchema)
def create_setting(setting: SettingCreate, db: Session = Depends(get_db)):
    # Check if the user exists
    user = db.query(User).filter(User.user_id == setting.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Check if settings already exist for this user
    existing_setting = db.query(Settings).filter(Settings.user_id == setting.user_id).first()
    if existing_setting:
        raise HTTPException(status_code=400, detail="Settings already exist for this user")
    
    db_setting = Settings(**setting.dict())
    db.add(db_setting)
    db.commit()
    db.refresh(db_setting)
    return db_setting

@router.get("/{user_id}", response_model=SettingSchema)
def read_setting(user_id: int, db: Session = Depends(get_db)):
    db_setting = db.query(Settings).filter(Settings.user_id == user_id).first()
    if db_setting is None:
        raise HTTPException(status_code=404, detail="Settings not found")
    return db_setting

@router.put("/{user_id}", response_model=SettingSchema)
def update_setting(user_id: int, setting: SettingCreate, db: Session = Depends(get_db)):
    db_setting = db.query(Settings).filter(Settings.user_id == user_id).first()
    if db_setting is None:
        raise HTTPException(status_code=404, detail="Settings not found")
    
    for key, value in setting.dict().items():
        setattr(db_setting, key, value)
    
    db.commit()
    db.refresh(db_setting)
    return db_setting

@router.delete("/{user_id}")
def delete_setting(user_id: int, db: Session = Depends(get_db)):
    db_setting = db.query(Settings).filter(Settings.user_id == user_id).first()
    if db_setting is None:
        raise HTTPException(status_code=404, detail="Settings not found")
    
    db.delete(db_setting)
    db.commit()
    return {"message": "Settings deleted successfully"}