# src/models/character.py
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base

class Character(Base):
    __tablename__ = "characters"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    play_id = Column(Integer, ForeignKey("plays.id"), nullable=False)
    voice_config = Column(Text)  # JSON string for voice settings
    
    # Relationships
    play = relationship("Play", back_populates="characters")
    dialogues = relationship("Dialogue", back_populates="character")
    directions = relationship("StageDirection", back_populates="character")

    def __repr__(self):
        return f"<Character {self.name}>"