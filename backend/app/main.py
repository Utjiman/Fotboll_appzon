from fastapi import FastAPI
from app.routers import users
from app.routers import posts




app = FastAPI()

# Använd router
app.include_router(users.router)
app.include_router(posts.router)

@app.get("/")
def root():
    return {"message": "Välkommen till Football Community API 🚀"}

@app.get("/posts")  
def root():
    return {"stuff": "dina posts"}
