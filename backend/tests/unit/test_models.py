# tests/unit/test_models.py
import pytest
from src.models import Play, Character, Act, Scene, Dialogue

def test_create_play(test_db):
    # Create a play
    play = Play(
        title="Hamlet",
        author="William Shakespeare",
        description="The Tragedy of Hamlet, Prince of Denmark"
    )
    test_db.add(play)
    test_db.commit()
    test_db.refresh(play)
    
    assert play.id is not None
    assert play.title == "Hamlet"
    assert play.author == "William Shakespeare"

def test_create_character(test_db):
    # First create a play
    play = Play(
        title="Hamlet",
        author="William Shakespeare"
    )
    test_db.add(play)
    test_db.commit()
    
    # Create a character
    character = Character(
        name="Hamlet",
        description="Prince of Denmark",
        play_id=play.id,
        voice_config='{"pitch": 1.0, "speed": 1.0}'
    )
    test_db.add(character)
    test_db.commit()
    
    assert character.id is not None
    assert character.name == "Hamlet"
    assert character.play_id == play.id

def test_play_character_relationship(test_db):
    # Create play with character
    play = Play(
        title="Hamlet",
        author="William Shakespeare"
    )
    test_db.add(play)
    test_db.commit()
    
    character = Character(
        name="Hamlet",
        play_id=play.id
    )
    test_db.add(character)
    test_db.commit()
    
    # Test relationship
    assert len(play.characters) == 1
    assert play.characters[0].name == "Hamlet"