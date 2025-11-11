from pydantic import BaseModel
from datetime import datetime

# Basmodell – vad som krävs för att skapa ett inlägg
class PostBase(BaseModel):
    user_id: int
    team_id: int
    content: str

# Modell för POST /posts (skapa inlägg)
class PostCreate(PostBase):
    pass

# Modell för att returnera ett inlägg via GET
class Post(PostBase):
    id: int
    created_at: datetime
    likes: int

    class Config:
        orm_mode = True  # gör att SQLAlchemy-modellen kan konverteras direkt till Pydantic
