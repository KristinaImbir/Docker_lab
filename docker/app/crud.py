from sqlalchemy.orm import Session
from app.models import Item

def create_item(db: Session, name: str):
    item = Item(name=name)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

def get_items(db: Session):
    return db.query(Item).all()
