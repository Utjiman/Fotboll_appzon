from pydantic import BaseModel
from datetime import datetime

# Basmodell – definierar vilka fält som finns för ett inlägg
class PostBase(BaseModel):
    user_id: int       # ID på användaren som postar
    team_id: int       # ID på laget inlägget tillhör
    content: str       # Själva texten i inlägget

# Modell för POST /posts (när man skapar inlägg)
class PostCreate(PostBase):
    pass  # Ärver allt från PostBase (kan utökas senare om man vill ha extra validering)

# Modell för att returnera ett inlägg via GET
class Post(PostBase):
    id: int            # Inläggets ID i databasen
    created_at: datetime  # När inlägget skapades
    likes: int         # Antal gillningar

    class Config:
        orm_mode = True  # Gör att SQLAlchemy-objekt konverteras automatiskt till Pydantic-modeller
