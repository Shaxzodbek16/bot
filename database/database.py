import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import load_config

config = load_config(".env")
DATABASE_URL = f"sqlite:///{config.db.database}"

engine = create_engine(
    DATABASE_URL, 
    connect_args={"check_same_thread": False}  # Needed for SQLite
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# For raw SQLite3 operations if needed
def get_sqlite_connection():
    conn = sqlite3.connect(config.db.database)
    conn.row_factory = sqlite3.Row
    return conn