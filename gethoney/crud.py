from models import Honeypot, HoneypotResponse

from gethoney.db import Database


def create_honeypot(honeypot: Honeypot, db: Database) -> HoneypotResponse:
    db.curr.execute(
        """INSERT INTO honeypots
        (name, url, description)
        VALUES (?, ?, ?) """,
        (honeypot.name, honeypot.url, honeypot.description),
    )
    db.conn.commit()
    new_id = db.curr.lastrowid
    response = HoneypotResponse(id=new_id, name=honeypot.name, url=honeypot.url, description=honeypot.description)
    return response


def read_honeypot(id_: int, db: Database) -> HoneypotResponse:
    data = db._select_row_by_id(id_)
    if data:
        honeypot = HoneypotResponse(id=data[0], name=data[1], url=data[2], description=data[3])
        return honeypot


def update_honeypot(honeypot: Honeypot, id_: int, db: Database) -> HoneypotResponse:
    params = [honeypot.name, honeypot.url, honeypot.description, id_]
    db.curr.execute("UPDATE honeypots SET name = ?, url = ?, description = ? WHERE id == ?", (params))
    db.conn.commit()
    data = db._select_row_by_id(id_)
    if data:
        honeypot = HoneypotResponse(id=data[0], name=data[1], url=data[2], description=data[3])
        return honeypot


def delete_honeypot(id_: int, db: Database) -> None:
    data = db._select_row_by_id(id_)
    if data:
        db.curr.execute(
            """DELETE FROM honeypots
            WHERE id == ?""",
            (id_,),
        )
        db.conn.commit()


def list_honeypots(db: Database) -> list[HoneypotResponse]:
    data = db.curr.execute("SELECT * FROM honeypots").fetchall()
    honeypots = [
        HoneypotResponse(id=honeypot[0], name=honeypot[1], url=honeypot[2], description=honeypot[3])
        for honeypot in data
    ]
    return honeypots
