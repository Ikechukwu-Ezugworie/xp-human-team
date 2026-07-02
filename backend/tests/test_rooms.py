import pytest
from fastapi.testclient import TestClient

def test_list_rooms(client):
    response = client.get("/api/rooms")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_room(client):
    response = client.post("/api/rooms", json={"name": "TestRoom", "description": "Test"})
    assert response.status_code in [200, 201]

def test_get_room_not_found(client):
    response = client.get("/api/rooms/999")
    assert response.status_code == 404
