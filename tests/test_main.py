import pytest
from fastapi.testclient import TestClient
from pydantic import ValidationError

from gethoney.crud import Database
from gethoney.main import app, get_db
from gethoney.models import Honeypot

test_db = "file::memory:?cache=shared"


def override_db():
    db = Database(test_db)
    db.create_honeypot(Honeypot(name="test", url="http://12.12.1.1", description="test"))
    yield db


app.dependency_overrides[get_db] = override_db

client = TestClient(app)

#
# Create
#


def test_create_honeypot():
    honeypot = Honeypot(name="test", url="http://12.12.1.1", description="test")
    data = honeypot.dict()
    response = client.post("/honeypots/", json=data)
    assert response.status_code == 201
    assert response.json() == data


def test_create_honeypot_invalid_url():
    with pytest.raises(ValidationError):
        Honeypot(name="test", url="http://12.1", description="test")


#
# List
#


def test_list_honeypots():
    response = client.get("/honeypots/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


#
# Read
#


def test_get_honeypot():
    response = client.get("/honeypots/1")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)


def test_get_nonexistent_honeypot():
    response = client.get("/honeypots/100")
    assert response.status_code == 404
    assert isinstance(response.json(), dict)


#
# Update
#


def test_update_honeypot():
    honeypot = Honeypot(name="bob2", url="http://1.2.3.4", description="test")
    hp_data = honeypot.dict()
    payload = client.put("/honeypots/1", json=hp_data)
    response = client.get("/honeypots/1")
    assert payload.status_code == 200
    assert response.status_code == 200


def test_update_nonexistent_honeypot():
    honeypot = Honeypot(name="bob2", url="http://1.2.3.4", description="test")
    hp_data = honeypot.dict()
    payload = client.put("/honeypots/100", json=hp_data)
    assert payload.status_code == 404


#
# Delete
#


def test_delete_honeypot():
    response = client.delete("/honeypots/1")
    assert response.status_code == 204


def test_delete_nonexistent_honeypot():
    response = client.delete("/honeypots/100")
    assert response.status_code == 404
