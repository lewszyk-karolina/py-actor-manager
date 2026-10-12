import sqlite3
from app.models import Actor


class ActorManager():
    def __init__(self, db_name, table_name):
        self._db_name = sqlite3.connect(db_name)
        self._table_name = table_name


    def create(self, first_name, last_name):
        cur = self._db_name.cursor()
        cur.execute(f"INSERT INTO {self._table_name} (first_name, last_name) VALUES (?, ?)",
                    (first_name, last_name)
                    )
        self._db_name.commit()

    def all(self):
        cur = self._db_name.cursor()
        cur.execute(f"SELECT id, first_name, last_name FROM {self._table_name}")
        rows = cur.fetchall()

        actors = []
        for row in rows:
            actors.append(Actor(id=row[0], first_name=row[1], last_name=row[2]))

        return actors

    def update(self, pk, new_first_name, new_last_name):
        cur = self._db_name.cursor()
        cur.execute(
            f"UPDATE {self._table_name} SET first_name = ?, last_name = ? WHERE id = ?",
            (new_first_name, new_last_name, pk)
        )
        self._db_name.commit()

    def delete(self, pk):
        cur = self._db_name.cursor()
        cur.execute(
            f"DELETE FROM {self._table_name} WHERE id = ?",
            (pk,)
        )
        self._db_name.commit()
