from fastapi import FastAPI
from fastapi.testclient import TestClient
from gethoney.main import app
from gethoney.models import Honeypot

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


#TODO: Fix assert response as list of Honeypots, not just list
def test_get_honeypots():
    response = client.get("/honeypots/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)



def test_create_honeypots():
    honeypot = Honeypot(name="test",url="http://12.12.1.1", description="test")
    data = [honeypot.dict()]

    response = client.post("/honeypots/", json=data)
    assert response.status_code == 201
    assert response.json() == data
