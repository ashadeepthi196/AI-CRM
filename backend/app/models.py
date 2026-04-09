from sqlalchemy import Column, Integer, String, Text
from .database import Base

class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)
    doctor_name = Column(String)
    interaction_type = Column(String)
    notes = Column(Text)
    follow_up = Column(String)