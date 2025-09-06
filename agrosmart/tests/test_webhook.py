import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_webhook_verification():
    response = client.get("/webhook/?hub.mode=subscribe&hub.verify_token=verify_token&hub.challenge=123")
    assert response.status_code == 200

def test_receive_message():
    payload = {"object": "whatsapp_business_account", "entry": []}
    response = client.post("/webhook/", json=payload)
    assert response.status_code == 200