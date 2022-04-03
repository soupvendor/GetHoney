import sqlite3

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

    # TODO: Make Select * dynamic from list in initiator

    def select_from_db(self):
        self.curr.execute("SELECT * FROM honeypots")
        data = self.curr.fetchall()
        return data
