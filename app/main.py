from fastapi import FastAPI
from app.routes import items, users

app = FastAPI()

app.include_router(items.router)
app.include_router(users.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)