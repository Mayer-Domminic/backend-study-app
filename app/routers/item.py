from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from ..database.db import get_db
from ..models.item import Item
from ..schemas.item import ItemCreate, Item as ItemSchema

router = APIRouter(prefix="/items", tags=["items"])

@router.post("/", response_model=ItemSchema)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = Item(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@router.get("/", response_model=List[ItemSchema])
def read_items(
    user_id: int,
    tag_id: Optional[int] = None,
    difficulty: Optional[str] = None,
    name: Optional[str] = None,
    number: Optional[int] = None,
    src: Optional[str] = None,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    query = db.query(Item).filter(Item.user_id == user_id)
    
    if tag_id:
        query = query.filter(Item.tag_id == tag_id)
    if difficulty:
        query = query.filter(Item.difficulty == difficulty)
    if name:
        query = query.filter(Item.name.ilike(f"%{name}%"))
    if number is not None:
        query = query.filter(Item.number == number)
    if src:
        query = query.filter(Item.src == src)
    
    items = query.offset(skip).limit(limit).all()
    return items

@router.get("/{item_id}", response_model=ItemSchema)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.item_id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@router.put("/{item_id}", response_model=ItemSchema)
def update_item(item_id: int, item: ItemCreate, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.item_id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    
    for key, value in item.model_dump().items():
        setattr(db_item, key, value)
    
    db.commit()
    db.refresh(db_item)
    return db_item

@router.delete("/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.item_id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return {"message": "Item deleted successfully"}