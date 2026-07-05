def auth_headers(client, username):
    response = client.post(
        "/api/auth/register", json={"username": username, "password": "pass123"}
    )
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


def make_room(client, headers, name):
    return client.post("/api/rooms/", json={"name": name}, headers=headers).json()


def test_send_and_get_messages(client):
    headers = auth_headers(client, "msg_user")
    room = make_room(client, headers, "MsgRoom")
    sent = client.post(
        f"/api/messages/{room['id']}", json={"content": "hi there"}, headers=headers
    )
    assert sent.status_code == 200
    assert sent.json()["author_name"] == "msg_user"
    messages = client.get(f"/api/messages/{room['id']}", headers=headers).json()
    assert messages[0]["content"] == "hi there"


def test_empty_message_rejected(client):
    headers = auth_headers(client, "msg_user2")
    room = make_room(client, headers, "MsgRoom2")
    response = client.post(
        f"/api/messages/{room['id']}", json={"content": "   "}, headers=headers
    )
    assert response.status_code == 400


def test_message_to_missing_room_rejected(client):
    headers = auth_headers(client, "msg_user3")
    response = client.post(
        "/api/messages/999", json={"content": "hello"}, headers=headers
    )
    assert response.status_code == 404


def test_message_pagination(client):
    headers = auth_headers(client, "msg_user4")
    room = make_room(client, headers, "MsgRoom4")
    for i in range(5):
        client.post(
            f"/api/messages/{room['id']}", json={"content": f"m{i}"}, headers=headers
        )
    page = client.get(
        f"/api/messages/{room['id']}?skip=0&limit=2", headers=headers
    ).json()
    assert len(page) == 2
