from fastapi import Depends, FastAPI, HTTPException

from gethoney.crud import Database
from gethoney.models import Honeypot

db_path = "../data/gethoney.db"

app = FastAPI()


def get_db():
    yield Database(db_path)


@app.get("/honeypots/{id}", status_code=200)
def get_honeypot(id: int, db: Database = Depends(get_db)) -> Honeypot:
    honeypot = db.read_honeypot(id)
    if not honeypot:
        raise HTTPException(status_code=404, detail="Honeypot not found.")
    else:
        return honeypot


@app.get("/honeypots/", status_code=200)
def list_honeypots(db: Database = Depends(get_db)) -> list[Honeypot]:
    return db.list_honeypots()


@app.post("/honeypots/", status_code=201)
def create_honeypot(honeypot: Honeypot, db: Database = Depends(get_db)) -> Honeypot:
    db.create_honeypot(honeypot)
    return honeypot


@app.delete("/honeypots/{honeypot_id}", status_code=200)
def delete_honeypot(honeypot_id: int, db: Database = Depends(get_db)) -> Honeypot:
    honeypot = db.read_honeypot(honeypot_id)
    if not honeypot:
        raise HTTPException(status_code=404, detail="Honeypot not found.")
    else:
        db.delete_honeypot(honeypot_id)
        return honeypot


@app.put("/honeypots/{honeypot_id}", status_code=200)
def update_honeypot(honeypot_id: int, update_data: Honeypot, db: Database = Depends(get_db)) -> Honeypot:
    data = db.update_honeypot(update_data, honeypot_id)
    if not data:
        raise HTTPException(status_code=404, detail="Honeypot not found.")
    else:
        return data
