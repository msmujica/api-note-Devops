from fastapi.testclient import TestClient

from app import app


client = TestClient(app)


def test_health():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Esta es la segunda app. V2"
    }