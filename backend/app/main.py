from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel

from .database import SessionLocal, engine, Base
from .schemas import InteractionCreate
from .tools import log_interaction, edit_interaction
from .agent import agent_flow
from . import models

from fastapi.middleware.cors import CORSMiddleware

# create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# ✅ CORS (important for React)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 🏠 Home
@app.get("/")
def home():
    return {"message": "Backend Running 🚀"}

# ➕ Create interaction
@app.post("/log")
def log(data: InteractionCreate, db: Session = Depends(get_db)):
    return log_interaction(data.dict(), db)

# ✏️ Edit interaction
@app.put("/edit/{id}")
def edit(id: int, data: InteractionCreate, db: Session = Depends(get_db)):
    return edit_interaction(id, data.dict(), db)

# 📋 Get all interactions
@app.get("/interactions")
def get_all(db: Session = Depends(get_db)):
    return db.query(models.Interaction).all()

# ❌ Delete interaction
@app.delete("/delete/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    item = db.query(models.Interaction).filter(models.Interaction.id == id).first()
    if item:
        db.delete(item)
        db.commit()
        return {"message": "Deleted successfully"}
    return {"error": "Interaction not found"}

# ✅ Chat Request Schema
class ChatRequest(BaseModel):
    input_text: str

# 🤖 AI Chat (FIXED)
@app.post("/chat")
def chat(data: ChatRequest):
    return agent_flow(data.input_text)