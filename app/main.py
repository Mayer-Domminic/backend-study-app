from fastapi import FastAPI
from .routers import user, item, attempt, settings
from .database.db import engine, Base
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # This is the default Vite dev server port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(user.router)
app.include_router(item.router)
app.include_router(attempt.router)
app.include_router(settings.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}