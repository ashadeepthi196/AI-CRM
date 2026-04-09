from pydantic import BaseModel

class InteractionCreate(BaseModel):
    doctor_name: str
    interaction_type: str
    notes: str
    follow_up: str

class InteractionResponse(InteractionCreate):
    id: int

    class Config:
        orm_mode = True