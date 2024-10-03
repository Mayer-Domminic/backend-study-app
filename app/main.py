from fastapi import FastAPI
from app.database.init_db import init_db
from app.routes import user_routes, problem_routes, attempt_routes

app = FastAPI()

@app.on_event("startup")
def startup_event():
    init_db()

app.include_router(user_routes.router, prefix="/api")
app.include_router(problem_routes.router, prefix="/api")
app.include_router(attempt_routes.router, prefix="/api")  # Include attempt routes
