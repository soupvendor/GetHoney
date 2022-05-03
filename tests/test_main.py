from fastapi.testclient import TestClient

from gethoney.crud import Database
from gethoney.main import app, get_db
from gethoney.models import Honeypot

test_db = "file::memory:?cache=shared"
db = Database(test_db)


def override_db():
    yield Database(test_db)


app.dependency_overrides[get_db] = override_db

client = TestClient(app)


def test_insert(db: Database):
    db.create_honeypot(Honeypot(name="test", url="http://12.12.1.1", description="test"))


def test_fetchall(db: Database):
    data = db.curr.execute("SELECT * FROM honeypots").fetchall()
    return data


def test_create_honeypots():
    honeypot = Honeypot(name="test", url="http://12.12.1.1", description="test")
    data = honeypot.dict()
    response = client.post("/honeypots/", json=data)
    assert response.status_code == 201
    assert response.json() == data


def test_list_honeypots():
    response = client.get("/honeypots/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_honeypot(db_path: str):
    db = Database(db_path)
    return db.list_honeypots()


test_insert(db)
print(test_fetchall(db))


# def test_update_honeypots():
#     honeypot = Honeypot(name="test", url="http://12.12.1.1", description="test")
#     data = [honeypot.dict()]
#     response = client.put("honeypots/18", json=data)
#     assert response.status_code == 200


# # def test_delete_honeypots():
# #     response = client.delete("/honeypots/18")
# #     assert response.status_code == 200
