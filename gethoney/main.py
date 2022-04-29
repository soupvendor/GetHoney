from fastapi import FastAPI

from gethoney.crud import Database
from gethoney.models import Honeypot

gethoney_db = "../data/gethoney.db"

db = Database(gethoney_db)
app = FastAPI()


@app.post("/honeypots/", status_code=201)
def create_honeypots(honeypots: list[Honeypot]):
    db.insert_into_db(honeypots)
    return honeypots


@app.get("/honeypots/")
def get_honeypots():
    return db.select_from_db()


@app.delete("/honeypots/{honeypot_id}", status_code=200)
def delete_honeypot(honeypot_id: int):
    return db.delete_honeypot(id)


@app.put("/honeypots/{honeypot_id}", status_code=200)
def update_honeypot(honeypot_id: int, honeypot: Honeypot, name=None, url=None, description=None):
    return db.update_honeypot(honeypot_id, honeypot, name, url, description)


@app.get("/honeypots/{id}", status_code=200)
def get_honeypot(id: int):
    print(id)
    return db.get_honeypot(id)
