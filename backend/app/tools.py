from .models import Interaction

def log_interaction(data, db):
    interaction = Interaction(**data)
    db.add(interaction)
    db.commit()
    db.refresh(interaction)
    return interaction


def edit_interaction(id, updated_data, db):
    obj = db.query(Interaction).filter(Interaction.id == id).first()
    if obj:
        for key, value in updated_data.items():
            setattr(obj, key, value)
        db.commit()
        return obj
    return None


# extra tools (for requirement)
def summarize_notes(text):
    return "Summary: " + text[:50]

def extract_entities(text):
    return {"doctor": "Detected"}

def suggest_followup(text):
    return "Follow-up in 2 weeks"