from fastapi import Depends, FastAPI

from gethoney.crud import Database
from gethoney.models import Honeypot

db_path = "../data/gethoney.db"

app = FastAPI()


def get_db():
    yield Database(db_path)


@app.get("/honeypots/{id}", status_code=200)
def get_honeypot(id: int, db: Database = Depends(get_db)):
    print(id)
    return db.read_honeypot(id)


@app.get("/honeypots/")
def list_honeypots(db: Database = Depends(get_db)):
    return db.list_honeypots()


#  TODO: Change from list of Honeypots to single Honeypot


@app.post("/honeypots/", status_code=201)
def create_honeypot(honeypot: Honeypot, db: Database = Depends(get_db)):
    db.create_honeypot(honeypot)
    return honeypot


@app.delete("/honeypots/{honeypot_id}", status_code=200)
def delete_honeypot(honeypot_id: int, db: Database = Depends(get_db)):
    return db.delete_honeypot(honeypot_id)


@app.put("/honeypots/{honeypot_id}", status_code=200)
def update_honeypot(honeypot_id: int, honeypot: Honeypot, db: Database = Depends(get_db)):
    return db.update_honeypot(honeypot, honeypot_id)
