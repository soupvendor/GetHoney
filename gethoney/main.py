from typing import Iterator

from fastapi import Depends, FastAPI, HTTPException, Response

from gethoney.crud import (
    create_honeypot,
    delete_honeypot,
    list_honeypots,
    read_honeypot,
    update_honeypot,
)
from gethoney.db import Database
from gethoney.models import Honeypot, HoneypotResponse

db_path = "../data/gethoney.db"

app = FastAPI()


def get_db() -> Iterator[Database]:
    yield Database(db_path)


@app.get("/honeypots/{honeypot_id}", status_code=200)
def get_honeypot(honeypot_id: int, db: Database = Depends(get_db)) -> HoneypotResponse:
    honeypot = read_honeypot(honeypot_id, db)
    if not honeypot:
        raise HTTPException(status_code=404, detail="Honeypot not found.")
    else:
        return honeypot


@app.get("/honeypots/", status_code=200)
def get_honeypots(db: Database = Depends(get_db)) -> list[HoneypotResponse]:
    return list_honeypots(db)


@app.post("/honeypots/", status_code=201)
def post_honeypot(honeypot: Honeypot, db: Database = Depends(get_db)) -> HoneypotResponse:
    return create_honeypot(honeypot, db)


@app.put("/honeypots/{honeypot_id}", status_code=200)
def put_honeypot(honeypot_id: int, update_data: Honeypot, db: Database = Depends(get_db)) -> HoneypotResponse:
    data = update_honeypot(update_data, honeypot_id, db)
    if not data:
        raise HTTPException(status_code=404, detail="Honeypot not found.")
    else:
        return data


@app.delete("/honeypots/{honeypot_id}", status_code=200)
def delete_honeypot_(honeypot_id: int, db: Database = Depends(get_db)) -> HoneypotResponse:
    honeypot = read_honeypot(honeypot_id, db)
    if not honeypot:
        return Response(status_code=404)
    else:
        delete_honeypot(honeypot_id, db)
        return Response(status_code=204)
