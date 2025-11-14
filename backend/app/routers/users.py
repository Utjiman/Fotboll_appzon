from fastapi import APIRouter

# Skapa en router-instans för /users
router = APIRouter(
    prefix="/users",   # Alla endpoints börjar med /users
    tags=["Users"]     # För gruppering i Swagger UI
)

# En enkel test-route
@router.get("/")
def get_users():
    """Returnerar testdata för användare"""
    return {"message": "Här kommer användarna!"}
