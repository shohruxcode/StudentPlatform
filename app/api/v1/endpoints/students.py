from fastapi import APIRouter

# Mana shu qator bo'lishi shart va nomi aynan 'router' bo'lishi kerak
router = APIRouter()

@router.get("/")
async def get_students():
    return {"message": "Barcha talabalar ro'yxati"}