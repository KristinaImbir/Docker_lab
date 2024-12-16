import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Читаем URL базы данных из переменных окружения
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()