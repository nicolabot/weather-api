import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_health(client):
    resp = client.get("/health")
    assert resp.status_code == 200

def test_weather_valid_city(client):
    resp = client.get("/weather/stockholm")
    assert resp.status_code == 200
    data = resp.get_json()
    assert "temperature" in data

def test_weather_invalid_city(client):
    resp = client.get("/weather/atlantis")
    assert resp.status_code == 404

def test_alerts_valid_city(client):
    resp = client.get("/alerts/stockholm")
    assert resp.status_code == 200
