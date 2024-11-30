# src/routes/audio.py
from fastapi import APIRouter

router = APIRouter(prefix="/audio", tags=["audio"])

@router.get("/")
async def get_audio():
    return []