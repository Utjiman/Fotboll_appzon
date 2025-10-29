from fastapi import FastAPI
from app.routers import users


app = FastAPI()

# Använd router
app.include_router(users.router)

@app.get("/")
def root():
    return {"message": "Välkommen till Football Community API 🚀"}

@app.get("/posts")  
def root():
    return {"stuff": "dina posts"}
