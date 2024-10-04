# backend-study-app

on windows::
python -m venv .venv
.\.venv\Scripts\activate
wsl: source .venv/bin/activate

pip install -r requirements.txt
pip freeze > requirements.txt

uvicorn app.main:app --reload

cd study-app
npm install
npm run dev


# Features:
## weekly recap
## email notis in the morning (newsletter style)
## schedule X_item @ 4:00PM
## todo's for review


react-problemsolver/
├── src/
│   ├── components/
│   │   ├── ui/
│   │   │   ├── button.tsx
│   │   │   ├── card.tsx
│   │   │   ├── dialog.tsx
│   │   │   ├── input.tsx
│   │   │   └── label.tsx
│   │   ├── auth/
│   │   │   ├── login-button.tsx
│   │   │   ├── register-button.tsx
│   │   │   ├── login-form.tsx
│   │   │   └── register-form.tsx
│   │   └── landing-card.tsx
│   ├── lib/
│   │   └── api.ts
│   ├── App.tsx
│   ├── index.tsx
│   └── index.css
├── package.json
└── vite.config.ts