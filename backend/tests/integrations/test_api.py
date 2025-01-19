# tests/integration/test_api.py
import pytest
from fastapi import status

def test_create_play(client):
    response = client.post(
        "/api/v1/plays/",
        json={
            "title": "Hamlet",
            "author": "William Shakespeare",
            "content": "To be, or not to be...",
            "description": "The Tragedy of Hamlet"
        }
    )
    
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["title"] == "Hamlet"
    assert "id" in data

def test_get_plays(client):
    # First create a play
    client.post(
        "/api/v1/plays/",
        json={
            "title": "Hamlet",
            "author": "William Shakespeare",
            "content": "To be, or not to be...",
            "description": "The Tragedy of Hamlet"
        }
    )
    
    response = client.get("/api/v1/plays/")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert len(data) > 0
    assert data[0]["title"] == "Hamlet"

def test_get_play_not_found(client):
    response = client.get("/api/v1/plays/999")
    assert response.status_code == status.HTTP_404_NOT_FOUND

def test_update_play(client):
    # Create a play first
    create_response = client.post(
        "/api/v1/plays/",
        json={
            "title": "Hamlet",
            "author": "William Shakespeare",
            "content": "To be, or not to be...",
            "description": "The Tragedy of Hamlet"
        }
    )
    play_id = create_response.json()["id"]
    
    # Update the play
    update_response = client.put(
        f"/api/v1/plays/{play_id}",
        json={
            "title": "Hamlet - Updated",
            "author": "William Shakespeare",
            "description": "Updated description"
        }
    )
    
    assert update_response.status_code == status.HTTP_200_OK
    data = update_response.json()
    assert data["title"] == "Hamlet - Updated"