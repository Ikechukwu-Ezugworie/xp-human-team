def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200

def test_register_user(client):
    response = client.post("/api/auth/register", json={"username": "testuser", "password": "testpass"})
    assert response.status_code == 200

def test_list_rooms(client):
    response = client.get("/api/rooms")
    assert response.status_code == 200
