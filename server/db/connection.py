from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

def execute_sql(query: str):
    with engine.connect() as conn:
        result = conn.execute(text(query))
        return [dict(row) for row in result.mappings()]
