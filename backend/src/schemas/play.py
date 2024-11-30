# src/schemas/play.py
from pydantic import BaseModel
from typing import Optional

class PlayBase(BaseModel):
    title: str
    author: str
    content: str
    description: Optional[str] = None

class PlayCreate(PlayBase):
    pass

class Play(PlayBase):
    id: int
    
    class Config:
        from_attributes = True