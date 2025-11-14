from fastapi import FastAPI
from app.routers import users, posts  # Importerar routrar (endpoints) för användare och inlägg
from app import models, database

models.Base.metadata.create_all(bind=database.engine)

# Skapar huvudapplikationen (FastAPI-instansen)
app = FastAPI(
    title="Football Community API",
    description="API för fotbollscommunity med användare, lag och inlägg.",
    version="1.0.0"
)

# Registrerar routrarna så att deras endpoints blir aktiva i API:t
app.include_router(users.router)
app.include_router(posts.router)

# Root-endpoint – test eller välkomstmeddelande
@app.get("/")
def root():
    return {"message": "Välkommen till Football Community API 🚀"}

# En enkel test-endpoint för posts (kan tas bort när riktig logik finns)
@app.get("/posts")
def root_posts():
    return {"stuff": "dina posts"}


