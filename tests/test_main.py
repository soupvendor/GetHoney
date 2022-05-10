from typing import Iterator

import pytest
from fastapi.testclient import TestClient
from pydantic import ValidationError

from gethoney.crud import Database
from gethoney.main import app, get_db
from gethoney.models import Honeypot

test_db = "file::memory:?cache=shared"


def override_db() -> Iterator[Database]:
    db = Database(test_db)
    db.create_honeypot(Honeypot(name="test", url="http://12.12.1.1", description="test"))
    db.create_honeypot(Honeypot(name="test2", url="http://12.12.1.2", description="test2"))
    yield db


app.dependency_overrides[get_db] = override_db

client = TestClient(app)

#
# Create
#


def test_create_honeypot() -> None:
    data = {"name": "test", "url": "http://12.12.1.1", "description": "test"}
    response = client.post("/honeypots/", json=data)
    data["id"] = 3
    assert response.status_code == 201
    assert response.json() == data


def test_create_honeypot_invalid_url() -> None:
    with pytest.raises(ValidationError):
        Honeypot(name="test", url="http://12.1", description="test")


#
# List
#


def test_list_honeypots() -> None:
    response = client.get("/honeypots/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 2


#
# Read
#


def test_get_honeypot() -> None:
    response = client.get("/honeypots/1")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)


def test_get_nonexistent_honeypot() -> None:
    response = client.get("/honeypots/100")
    assert response.status_code == 404
    assert isinstance(response.json(), dict)


#
# Update
#


def test_update_honeypot() -> None:
    data = {"name": "bob2", "url": "http://1.2.3.4", "description": "test"}
    response = client.put("/honeypots/1", json=data)
    data["id"] = 1
    assert response.json() == data
    assert response.status_code == 200


def test_update_nonexistent_honeypot() -> None:
    data = {"name": "bob", "url": "http://1.2.3.4", "description": "test"}
    response = client.put("/honeypots/100", json=data)
    assert response.status_code == 404


#
# Delete
#


def test_delete_honeypot() -> None:
    response = client.delete("/honeypots/1")
    assert response.status_code == 204


def test_delete_nonexistent_honeypot() -> None:
    response = client.delete("/honeypots/100")
    assert response.status_code == 404
