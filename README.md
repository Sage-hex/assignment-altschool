# Library Management App (SQLAlchemy + PostgreSQL)

A simple CRUD API for managing books and members, built with FastAPI and SQLAlchemy ORM.

## Setup

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set your PostgreSQL connection string:

```bash
export DATABASE_URL='postgresql+psycopg2://postgres:postgres@localhost:5432/library_db'
```

4. Run the app:

```bash
uvicorn app.main:app --reload
```

## Endpoints

- `POST /books`
- `GET /books`
- `GET /books/{book_id}`
- `PUT /books/{book_id}`
- `DELETE /books/{book_id}`

- `POST /members`
- `GET /members`
- `GET /members/{member_id}`
- `PUT /members/{member_id}`
- `DELETE /members/{member_id}`

## Notes

- Uses SQLAlchemy ORM models and PostgreSQL via `DATABASE_URL` environment variable.
