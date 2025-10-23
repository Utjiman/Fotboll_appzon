from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Football Community API is running!"}
