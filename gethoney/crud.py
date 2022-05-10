import sqlite3

from gethoney.models import Honeypot, HoneypotResponse

# import json
# import requests


class Database:
    def __init__(self, db_path: str) -> None:
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.curr = self.conn.cursor()
        self.curr.execute(
            """CREATE TABLE IF NOT EXISTS honeypots
            (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, url TEXT, description TEXT)"""
        )
        self.curr.execute(
            """CREATE TABLE IF NOT EXISTS logs
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            honeypot_id INTEGER,
            FOREIGN KEY (honeypot_id) REFERENCES honeypots (id))"""
        )

    def db_data(self, id_) -> list:
        data = self.curr.execute("SELECT * FROM honeypots WHERE id == ?", (id_,)).fetchone()
        return data

    def create_honeypot(self, honeypot: Honeypot) -> HoneypotResponse:
        self.curr.execute(
            """INSERT INTO honeypots
            (name, url, description)
            VALUES (?, ?, ?) """,
            (honeypot.name, honeypot.url, honeypot.description),
        )
        self.conn.commit()
        new_id = self.curr.lastrowid
        response = HoneypotResponse(id=new_id, name=honeypot.name, url=honeypot.url, description=honeypot.description)
        return response

    def list_honeypots(self) -> list[HoneypotResponse]:
        data = self.curr.execute("SELECT * FROM honeypots").fetchall()
        honeypots = (
            HoneypotResponse(id=honeypot[0], name=honeypot[1], url=honeypot[2], description=honeypot[3])
            for honeypot in data
        )
        return honeypots

    # def retrieve_logs(self, honeypot: Honeypot):
    #     fetch_url_id = self.curr.execute("SELECT url, id FROM honeypots WHERE name == ?", (honeypot.name,)).fetchall()
    #     url = fetch_url_id[0][0]
    #     id = fetch_url_id[0][1]

    #     request = requests.get(url)
    #     data = request.json()

    #     self.curr.executemany(
    #         """INSERT INTO logs
    #         (name, honeypot_id)
    #         VALUES (?, ?)""",
    #         [(item["name"], id) for item in data],
    #     )
    #     self.conn.commit()

    def update_honeypot(self, honeypot: Honeypot, id_: int) -> HoneypotResponse:
        params = [honeypot.name, honeypot.url, honeypot.description, id_]
        self.curr.execute("UPDATE honeypots SET name = ?, url = ?, description = ? WHERE id == ?", (params))
        self.conn.commit()
        data = self.db_data(id_)
        if data:
            honeypot = HoneypotResponse(id=data[0], name=data[1], url=data[2], description=data[3])
            return honeypot

    def delete_honeypot(self, id_: int) -> None:
        data = self.db_data(id_)
        if data:
            self.curr.execute(
                """DELETE FROM honeypots
                WHERE id == ?""",
                (id_,),
            )
            self.conn.commit()

    def read_honeypot(self, id_: int) -> HoneypotResponse:
        data = self.db_data(id_)
        if data:
            honeypot = HoneypotResponse(id=data[0], name=data[1], url=data[2], description=data[3])
            return honeypot
