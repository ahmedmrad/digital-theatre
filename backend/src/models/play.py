# src/models/play.py
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
import enum
from ..database import Base

class DirectionType(enum.Enum):
    MOVEMENT = "movement"
    EMOTION = "emotion"
    ACTION = "action"
    SETTING = "setting"
    LIGHTING = "lighting"
    SOUND = "sound"
    PROP = "prop"
    GENERAL = "general"

class Play(Base):
    __tablename__ = "plays"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True, nullable=False)
    author = Column(String(255), nullable=False)
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    acts = relationship("Act", back_populates="play", cascade="all, delete-orphan")
    characters = relationship("Character", back_populates="play", cascade="all, delete-orphan")

class Act(Base):
    __tablename__ = "acts"
    
    id = Column(Integer, primary_key=True, index=True)
    number = Column(Integer, nullable=False)
    title = Column(String(255))
    play_id = Column(Integer, ForeignKey("plays.id"), nullable=False)
    
    # Relationships
    play = relationship("Play", back_populates="acts")
    scenes = relationship("Scene", back_populates="act", cascade="all, delete-orphan")

class Scene(Base):
    __tablename__ = "scenes"
    
    id = Column(Integer, primary_key=True, index=True)
    number = Column(Integer, nullable=False)
    title = Column(String(255))
    act_id = Column(Integer, ForeignKey("acts.id"), nullable=False)
    
    # Relationships
    act = relationship("Act", back_populates="scenes")
    dialogues = relationship("Dialogue", back_populates="scene", cascade="all, delete-orphan")
    directions = relationship("StageDirection", back_populates="scene")

class Dialogue(Base):
    __tablename__ = "dialogues"
    
    id = Column(Integer, primary_key=True, index=True)
    scene_id = Column(Integer, ForeignKey("scenes.id"), nullable=False)
    character_id = Column(Integer, ForeignKey("characters.id"), nullable=False)
    line_number = Column(Integer, nullable=False)
    content = Column(Text, nullable=False)
    
    # Relationships
    scene = relationship("Scene", back_populates="dialogues")
    character = relationship("Character", back_populates="dialogues")
    directions = relationship("StageDirection", back_populates="dialogue")

class StageDirection(Base):
    __tablename__ = "stage_directions"
    
    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text, nullable=False)
    direction_type = Column(Enum(DirectionType), nullable=False)
    
    scene_id = Column(Integer, ForeignKey("scenes.id"), nullable=True)
    dialogue_id = Column(Integer, ForeignKey("dialogues.id"), nullable=True)
    character_id = Column(Integer, ForeignKey("characters.id"), nullable=True)
    
    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    scene = relationship("Scene", back_populates="directions")
    dialogue = relationship("Dialogue", back_populates="directions")
    character = relationship("Character", back_populates="directions")