# src/routes/characters.py
from fastapi import APIRouter

router = APIRouter(prefix="/characters", tags=["characters"])

@router.get("/")
async def get_characters():
    return []