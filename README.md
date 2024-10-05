# backend-study-app

on windows::
python -m venv .venv
.\.venv\Scripts\activate
wsl: source .venv/bin/activate

pip install -r requirements.txt
pip freeze > requirements.txt

uvicorn app.main:app --reload

npm install
make a postgres db, make a user named github_user
make the password abc123 and then it should work


python -m app.database.init_db

cd study-app
npm install
npm run dev


# Features:
## weekly recap
## email notis in the morning (newsletter style)
## schedule X_item @ 4:00PM
## todo's for review
