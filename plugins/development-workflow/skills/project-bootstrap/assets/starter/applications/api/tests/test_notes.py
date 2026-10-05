from uuid import uuid4

from fastapi.testclient import TestClient

from notes.main import app

ORIGIN = {"origin": "http://localhost:3000"}


def account(client):
    data = {"email": f"{uuid4()}@example.com", "password": "test-password-123"}
    assert client.post("/api/auth/register", json=data, headers=ORIGIN).status_code == 201
    return data


def test_auth_persistence_and_ownership():
    with TestClient(app) as first, TestClient(app) as second:
        assert first.get("/api/notes").status_code == 401
        credentials = account(first)
        assert first.post("/api/auth/register", json=credentials, headers=ORIGIN).status_code == 409
        assert (
            first.post(
                "/api/auth/login",
                json={**credentials, "password": "incorrect-password"},
                headers=ORIGIN,
            ).status_code
            == 401
        )
        assert first.post("/api/notes", json={"title": " "}, headers=ORIGIN).status_code == 422
        result = first.post("/api/notes", json={"title": "Persisted"}, headers=ORIGIN)
        assert result.status_code == 201
        note_id = result.json()["id"]
        old_token = first.cookies.get("session")
        assert first.post("/api/auth/logout", headers=ORIGIN).status_code == 204
        assert first.get("/api/notes").status_code == 401
        first.cookies.set("session", old_token)
        assert first.get("/api/me").status_code == 401
        first.cookies.clear()
        assert first.post("/api/auth/login", json=credentials, headers=ORIGIN).status_code == 200
        assert first.get(f"/api/notes/{note_id}").json()["title"] == "Persisted"
        account(second)
        assert second.get("/api/notes").json() == []
        assert second.get(f"/api/notes/{note_id}").status_code == 404
        assert (
            second.post(
                "/api/notes", json={"title": "CSRF"}, headers={"origin": "https://evil.test"}
            ).status_code
            == 403
        )
        assert second.post("/api/notes", json={"title": "No origin"}).status_code == 403
