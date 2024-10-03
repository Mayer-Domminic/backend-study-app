# backend-study-app

on windows::
python -m venv .venv
.\.venv\Scripts\activate
wsl: source .venv/bin/activate

pip install -r requirements.txt
pip freeze > requirements.txt

uvicorn app.main:app --reload

│
├── /app
│   ├── /database            # Database setup
│   │   └── db.py
│   │   └── init_db.py
│   │
│   ├── /models              # SQLAlchemy models
│   │   └── user.py
│   │   └── problem.py
│   │   └── user_problem.py
│   │   └── attempt.py
│   │
│   ├── /crud                # Utility functions (CRUD operations)
│   │   └── user.py
│   │   └── problem.py
│   │   └── attempt.py
│   │
│   ├── /routes              # FastAPI routes
│   │   └── user_routes.py
│   │   └── problem_routes.py
│   │   └── attempt_routes.py
│   │
│   ├── /schemas             # Pydantic schemas for validation
│   │   └── user.py
│   │   └── problem.py
│   │   └── attempt.py
│   │
│   └── main.py              # FastAPI entry point
│
└── requirements.txt         # List of dependencies

https://chatgpt.com/share/66fee7be-8b78-8005-a2b3-33f6f92d90df