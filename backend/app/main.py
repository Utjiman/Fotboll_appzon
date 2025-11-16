from fastapi import FastAPI
from app.routers import users, posts   # Importerar dina routers
from app.database import Base, engine  # Base + engine MÅSTE komma härifrån

# 🔧 Skapa tabeller i databasen vid uppstart
Base.metadata.create_all(bind=engine)

# 🚀 Skapa själva FastAPI-appen
app = FastAPI(
    title="Football Community API",
    description="API för fotbollscommunity med användare, lag och inlägg.",
    version="1.0.0"
)

# 🔌 Registrera routers (endpoints)
app.include_router(users.router)
app.include_router(posts.router)

# 🌍 Start-endpoint
@app.get("/")
def root():
    return {"message": "Välkommen till Football Community API 🚀"}

# ❗ Temporär test-endpoint — kan tas bort sen
@app.get("/posts")
def root_posts():
    return {"stuff": "dina posts"}
