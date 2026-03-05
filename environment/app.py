from fastapi import FastAPI
from db import get_db

app = FastAPI()

@app.get("/health")
def health():
    db = get_db()
    return {"status": "ok"}
