from fastapi import APIRouter, Depends
from app.database import get_db
import psycopg

router = APIRouter()

@router.get("/items")
async def read_items(db: psycopg.AsyncConnection = Depends(get_db)):
    async with db.cursor() as cur:
        await cur.execute("SELECT * FROM items")
        items = await cur.fetchall()
    return items

@router.post("/items")
async def create_item(item: dict, db: psycopg.AsyncConnection = Depends(get_db)):
    async with db.cursor() as cur:
        await cur.execute(
            "INSERT INTO items (name, description) VALUES (%s, %s) RETURNING id",
            (item['name'], item.get('description'))
        )
        item_id = await cur.fetchone()
        await db.commit()
    return {"id": item_id['id'], **item}