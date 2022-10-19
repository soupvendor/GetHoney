import sqlite3


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

    def select_row_by_id(self, id_) -> list:
        data = self.curr.execute("SELECT * FROM honeypots WHERE id == ?", (id_,)).fetchone()
        return data

    def select_all_honeypots(self) -> list:
        data = self.curr.execute("SELECT * FROM honeypots").fetchall()
        return data
