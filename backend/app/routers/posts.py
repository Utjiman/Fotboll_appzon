from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app import models, database, schemas

router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)

# Hämta databas-session
get_db = database.get_db


@router.get("/{team_id}")
def get_posts(team_id: int, db: Session = Depends(get_db)):
    """Hämta alla inlägg för ett visst lag"""
    posts = db.query(models.Post).filter(models.Post.team_id == team_id).order_by(models.Post.created_at.desc()).all()
    return posts


@router.post("/")
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
    """Skapa ett nytt inlägg"""
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

