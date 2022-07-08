from sqlite3 import connect
from uuid import uuid4


class InMemorySQLiteDatabase:
    def __init__(self):
        self.uri = f"file:{str(uuid4())}?cache=shared&mode=memory"

    def events(self):
        with connect(self.uri, uri=True) as connection:
            return connection.execute("SELECT * FROM events").fetchall()

    def insert_event(self, timestamp: str, action: str):
        with connect(self.uri, uri=True) as connection:
            connection.execute("INSERT INTO events (timestamp, action) VALUES (?, ?)", (timestamp, action))
            connection.commit()
