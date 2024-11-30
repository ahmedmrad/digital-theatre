# src/routes/play.py
from fastapi import APIRouter, HTTPException
from typing import List
from ..schemas.play import Play, PlayCreate
from ..services.play import PlayService

router = APIRouter(prefix="/plays", tags=["plays"])

@router.get("/", response_model=List[Play])
async def get_plays():
    return []

@router.get("/{play_id}", response_model=Play)
async def get_play(play_id: int):
    return {
        "id": play_id,
        "title": "The Visa",
        "author": "Ahmed Mrad",
        "content": "Sample content",
        "description": "A play about immigration and identity"
    }