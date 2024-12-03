# src/models/audio.py
from sqlalchemy import Column, Integer, String, Float, ForeignKey, JSON
from sqlalchemy.orm import relationship
from ..database import Base

class AudioSegment(Base):
    __tablename__ = "audio_segments"
    
    id = Column(Integer, primary_key=True, index=True)
    dialogue_id = Column(Integer, ForeignKey("dialogues.id"), nullable=False)
    file_path = Column(String(255), nullable=False)  # Path to audio file
    duration = Column(Float, nullable=False)  # Duration in seconds
    start_time = Column(Float, nullable=False)  # Start time in the play
    waveform_data = Column(JSON)  # For visualization
    
    # Relationships
    dialogue = relationship("Dialogue", back_populates="audio")

class VoiceProfile(Base):
    __tablename__ = "voice_profiles"
    
    id = Column(Integer, primary_key=True, index=True)
    character_id = Column(Integer, ForeignKey("characters.id"), nullable=False)
    voice_id = Column(String(255), nullable=False)  # ID for the AI voice service
    pitch = Column(Float, default=1.0)
    speed = Column(Float, default=1.0)
    settings = Column(JSON)  # Additional voice settings
    
    # Relationships
    character = relationship("Character", back_populates="voice_profile")