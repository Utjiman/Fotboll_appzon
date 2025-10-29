from fastapi import APIRouter

# Skapa en router-instans
router = APIRouter(
    prefix="/users",
    tags=["users"]
)

# En enkel route för test
@router.get("/")
def get_users():
    return {"message": "Här kommer användarna!"}
