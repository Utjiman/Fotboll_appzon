from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app import models, database
from app.schemas.post_schema import PostCreate, Post

# Skapar en router för alla /posts-endpoints
router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)

# Hämtar databas-session via dependency injection
get_db = database.get_db


@router.get("/{team_id}")
def get_posts(team_id: int, db: Session = Depends(get_db)):
    """Hämta alla inlägg för ett specifikt lag"""
    posts = db.query(models.Post)\
              .filter(models.Post.team_id == team_id)\
              .order_by(models.Post.created_at.desc())\
              .all()

    if not posts:
        raise HTTPException(status_code=404, detail="Inga inlägg hittades för detta lag.")
    return posts


@router.post("/")
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    """Skapa ett nytt inlägg"""
    new_post = models.Post(**post.dict())  # Skapa Post-objekt från inkommande data
    db.add(new_post)
    db.commit()
    db.refresh(new_post)  # Uppdaterar objektet med ID och timestamp
    return new_post
