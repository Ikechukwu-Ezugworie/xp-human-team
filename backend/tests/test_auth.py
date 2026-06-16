import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app, get_db, Base

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)

def test_register_user():
    response = client.post("/api/auth/register", json={"username": "testuser", "password": "testpass"})
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_register_duplicate_user():
    client.post("/api/auth/register", json={"username": "user1", "password": "pass1"})
    response = client.post("/api/auth/register", json={"username": "user1", "password": "pass2"})
    assert response.status_code == 400

def test_login_success():
    client.post("/api/auth/register", json={"username": "user2", "password": "pass2"})
    response = client.post("/api/auth/login", json={"username": "user2", "password": "pass2"})
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_login_invalid_credentials():
    response = client.post("/api/auth/login", json={"username": "nouser", "password": "nopass"})
    assert response.status_code == 401
