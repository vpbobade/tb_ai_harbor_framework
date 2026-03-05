from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///./data.db"

engine = create_engine(DATABASE_URL)

def get_db():
    conn = engine.connect()
    return conn
