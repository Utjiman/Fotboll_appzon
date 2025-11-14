from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Enkel lokal databas (app.db kommer skapas automatiskt i backend-mappen)
SQLALCHEMY_DATABASE_URL = "sqlite:///./app.db"

# Skapa "engine" = kopplingen till databasen
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Session = används i varje request för att prata med databasen
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = grunden för alla modeller (t.ex. Post, User)
Base = declarative_base()

# Funktion för att skapa en databas-session i endpoints
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
