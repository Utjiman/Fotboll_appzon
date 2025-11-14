from sqlalchemy import Column, Integer, String, DateTime, func
from app.database import Base

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)

    # Lägg tillbaka kolumnerna korrekt
    user_id = Column(Integer, nullable=False)
    team_id = Column(Integer, nullable=False)

    content = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    likes = Column(Integer, default=0)
