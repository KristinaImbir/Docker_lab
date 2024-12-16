from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app import models, database, crud
from app.run_migrations import apply_migrations

app = FastAPI()

# Накатываем миграции
apply_migrations()

# Инициализация базы данных
models.Base.metadata.create_all(bind=database.engine)




# Маршруты
@app.get("/")
def read_root():
    return {"message": "Hello, Docker with FastAPI and PostgreSQL!"}

@app.post("/items/")
def create_item(name: str, db: Session = Depends(database.get_db)):
    item = crud.create_item(db=db, name=name)
    return {"id": item.id, "name": item.name}

@app.get("/items/")
def read_items(db: Session = Depends(database.get_db)):
    items = crud.get_items(db=db)
    return [{"id": item.id, "name": item.name} for item in items]
