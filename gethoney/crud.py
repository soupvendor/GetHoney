import sqlite3

import requests

from gethoney.models import Honeypot

# TODO: Make dynamic list with table names in initiation


class Database:
    def __init__(self, db_path: str):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.curr = self.conn.cursor()
        self.curr.execute(
            """CREATE TABLE IF NOT EXISTS honeypots
        (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, url TEXT, description TEXT)"""
        )

    def insert_into_db(self, honeypots: list[Honeypot]):
        self.curr.executemany(
            """INSERT INTO honeypots
                        (name, url, description)
                        VALUES (?, ?, ?) """,
            [(honeypot.name, honeypot.url, honeypot.description) for honeypot in honeypots],
        )

        self.conn.commit()
        self.curr.execute(
            """SELECT id FROM honeypots WHERE
                    (name) == VALUES (?) """,
            (honeypots[0].name),
        )
        data = self.curr.fetchall()
        return data

    # TODO: Make Select * dynamic from list in initiator

    def select_from_db(self):
        self.curr.execute("SELECT * FROM honeypots")
        data = self.curr.fetchall()
        return data

    def retrieve_logs(self, honeypot: Honeypot):
        logs = []

        fetch = self.curr.execute("""SELECT url FROM honeypots WHERE name == ? """, (honeypot,)).fetchall()
        data = self.curr.fetchall()

        return fetch
        request = requests.get("http://3.137.141.78/")
        data = request.json()

        for item in data:
            logs.append(item["name"])


gethoney_db = "../data/gethoney.db"
f = Database(gethoney_db)

print(f.retrieve_logs("string"))
