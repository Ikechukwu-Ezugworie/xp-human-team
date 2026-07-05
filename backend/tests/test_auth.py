def register(client, username="testuser", password="testpass"):
    return client.post("/api/auth/register", json={"username": username, "password": password})


def auth_headers(client, username="testuser"):
    response = register(client, username)
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200


def test_register_user(client):
    response = register(client, "alice")
    assert response.status_code == 200
    assert "access_token" in response.json()


def test_register_duplicate_rejected(client):
    register(client, "bob")
    response = register(client, "bob")
    assert response.status_code == 400


def test_login_invalid_credentials(client):
    response = client.post("/api/auth/login", json={"username": "ghost", "password": "nope"})
    assert response.status_code == 401


def test_rooms_require_auth(client):
    response = client.get("/api/rooms/")
    assert response.status_code == 401


def test_create_and_list_rooms(client):
    headers = auth_headers(client, "carol")
    created = client.post("/api/rooms/", json={"name": "standup"}, headers=headers)
    assert created.status_code == 200
    listed = client.get("/api/rooms/", headers=headers)
    assert listed.status_code == 200
    assert any(r["name"] == "standup" for r in listed.json())


def test_send_and_fetch_message(client):
    headers = auth_headers(client, "dave")
    room = client.post("/api/rooms/", json={"name": "dev-chat"}, headers=headers).json()
    sent = client.post(f"/api/messages/{room['id']}", json={"content": "hello"}, headers=headers)
    assert sent.status_code == 200
    assert sent.json()["author_name"] == "dave"
    fetched = client.get(f"/api/messages/{room['id']}", headers=headers)
    assert fetched.status_code == 200
    assert fetched.json()[0]["content"] == "hello"
