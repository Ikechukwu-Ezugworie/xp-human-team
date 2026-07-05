def auth_headers(client, username):
    response = client.post(
        "/api/auth/register", json={"username": username, "password": "pass123"}
    )
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


def test_list_rooms_requires_auth(client):
    assert client.get("/api/rooms/").status_code == 401


def test_create_and_get_room(client):
    headers = auth_headers(client, "room_owner")
    created = client.post(
        "/api/rooms/", json={"name": "TestRoom", "description": "Test"}, headers=headers
    )
    assert created.status_code == 200
    room_id = created.json()["id"]
    fetched = client.get(f"/api/rooms/{room_id}", headers=headers)
    assert fetched.status_code == 200
    assert fetched.json()["name"] == "TestRoom"


def test_duplicate_room_name_rejected(client):
    headers = auth_headers(client, "room_owner2")
    client.post("/api/rooms/", json={"name": "DupRoom"}, headers=headers)
    response = client.post("/api/rooms/", json={"name": "DupRoom"}, headers=headers)
    assert response.status_code == 400


def test_get_room_not_found(client):
    headers = auth_headers(client, "room_owner3")
    assert client.get("/api/rooms/999", headers=headers).status_code == 404
