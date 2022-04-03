from fastapi import FastAPI

from gethoney.crud import Database
from gethoney.models import Honeypot

gethoney_db = "../data/gethoney.db"

db = Database(gethoney_db)
app = FastAPI()


# curr.execute(
#     """CREATE TABLE IF NOT EXISTS logs
#     (id INTEGER PRIMARY KEY, log_id INTEGER, name TEXT))"""
# )


@app.post("/honeypots/", status_code=201)
def create_honeypots(honeypots: list[Honeypot]):
    db.insert_into_db(honeypots)
    return honeypots


@app.get("/honeypots/")
def get_honeypots():
    return db.select_from_db()


# @app.get("/honeypots/logs/")
# def get_logs(honeypot: list[], )


# @app.post("/honeypots/logs/")
# def create_logs(honeypot: Honeypot):
