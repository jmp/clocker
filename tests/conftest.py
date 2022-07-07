from sqlite3 import connect
from uuid import uuid4

from pytest import fixture


class InMemoryDatabase:
    def __init__(self, file: str):
        self.file = file

    def events(self):
        with connect(self.file, uri=True) as connection:
            return connection.execute("SELECT * FROM events").fetchall()

    def insert_event(self, timestamp: str, action: str):
        with connect(self.file, uri=True) as connection:
            connection.execute("INSERT INTO events (timestamp, action) VALUES (?, ?)", (timestamp, action))
            connection.commit()


@fixture
def database() -> InMemoryDatabase:
    return InMemoryDatabase(f"file:{str(uuid4())}?cache=shared&mode=memory")
