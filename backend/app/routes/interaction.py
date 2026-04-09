from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import SessionLocal

router = APIRouter()

# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ➕ Create
@router.post("/interactions")
def create_interaction(data: schemas.InteractionCreate, db: Session = Depends(get_db)):
    new_data = models.Interaction(**data.dict())
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return new_data

# 📋 Get all
@router.get("/interactions")
def get_all(db: Session = Depends(get_db)):
    return db.query(models.Interaction).all()

# ✏️ Update
@router.put("/interactions/{id}")
def update_interaction(id: int, data: schemas.InteractionCreate, db: Session = Depends(get_db)):
    item = db.query(models.Interaction).filter(models.Interaction.id == id).first()
    if item:
        item.doctor_name = data.doctor_name
        item.interaction_type = data.interaction_type
        item.notes = data.notes
        item.follow_up = data.follow_up
        db.commit()
        return item
    return {"error": "Not found"}

# ❌ Delete
@router.delete("/interactions/{id}")
def delete_interaction(id: int, db: Session = Depends(get_db)):
    item = db.query(models.Interaction).filter(models.Interaction.id == id).first()
    if item:
        db.delete(item)
        db.commit()
        return {"message": "Deleted"}
    return {"error": "Not found"}