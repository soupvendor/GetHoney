from fastapi import FastAPI
from gethoney.core.models import Honeypot
import sqlite3

conn = sqlite3.connect("../data/gethoney.db", check_same_thread=False)
curr = conn.cursor()
app = FastAPI()

curr.execute(
    """CREATE TABLE IF NOT EXISTS honeypots
    (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, url TEXT, description TEXT)"""
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/honeypots/")
def create_honeypots(honeypots: list[Honeypot]):

    curr.executemany(
        """INSERT INTO honeypots
                (name, url, description)
                VALUES (?, ?, ?) """,
        [(honeypot.name, honeypot.url, honeypot.description) for honeypot in honeypots],
    )
    conn.commit()


@app.get("/honeypots/")
def get_honeypots():
    curr.execute("SELECT * FROM honeypots")
    data = curr.fetchall()
    return data
