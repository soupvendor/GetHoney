from fastapi import FastAPI
from gethoney.models import Honeypot
from gethoney.crud import conn, curr
import requests

app = FastAPI()

curr.execute(
    """CREATE TABLE IF NOT EXISTS honeypots
    (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, url TEXT, description TEXT)"""
)

# curr.execute(
#     """CREATE TABLE IF NOT EXISTS logs
#     (id INTEGER PRIMARY KEY, log_id INTEGER, name TEXT))"""
# )


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/honeypots/", status_code=201)
def create_honeypots(honeypots: list[Honeypot]):

    curr.executemany(
        """INSERT INTO honeypots
                (name, url, description)
                VALUES (?, ?, ?) """,
        [(honeypot.name, honeypot.url, honeypot.description) for honeypot in honeypots],
    )
    conn.commit()
    return honeypots


@app.get("/honeypots/")
def get_honeypots():
    curr.execute("SELECT * FROM honeypots")
    data = curr.fetchall()
    return data


# @app.get("/honeypots/logs/")
# def get_logs(honeypot: list[], )


# @app.post("/honeypots/logs/")
# def create_logs(honeypot: Honeypot):
