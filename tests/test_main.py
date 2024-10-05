from fastapi.testclient import TestClient
from ..app.main import app

client = TestClient(app)

def test_register_user():
    response = client.post("/users/register", json={"username": "testuser", "email": "test@example.com", "password": "testpassword"})
    assert response.status_code == 200
    assert "User created successfully" in response.json().get("message")

def test_login_user():
    response = client.post("/users/login", json={"username": "testuser", "password": "testpassword"})
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_upload_document():
    with open("test.pdf", "rb") as file:
        response = client.post("/documents/upload", files={"file": file}, params={"class_id": 1})
        assert response.status_code == 200
        assert "Document processed and saved" in response.json().get("message")
