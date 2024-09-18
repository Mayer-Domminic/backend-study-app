import psycopg
from psycopg.rows import dict_row
from contextlib import asynccontextmanager

async def get_connection():
    return await psycopg.AsyncConnection.connect(
        "host=localhost dbname=postgres user=postgres password=abc123",
        row_factory=dict_row
    )

@asynccontextmanager
async def get_db():
    conn = await get_connection()
    try:
        yield conn
    finally:
        await conn.close()