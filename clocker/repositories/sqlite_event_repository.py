from datetime import datetime
from sqlite3 import connect
from typing import Optional

from ..event import Event
from ..action import Action
from ..repositories import EventRepository


CREATE_SQL = """
    CREATE TABLE IF NOT EXISTS events (
        timestamp PRIMARY KEY NOT NULL,
        action NOT NULL
    )
"""
INSERT_SQL = "INSERT INTO events (timestamp, action) VALUES (?, ?)"
SELECT_SQL = "SELECT timestamp, action FROM events ORDER BY timestamp DESC LIMIT 1"


class SQLiteEventRepository(EventRepository):
    def __init__(self, path: str):
        self._connection = connect(path)
        self._connection.execute(CREATE_SQL)

    def insert_event(self, event: Event):
        row = (event.timestamp.isoformat(), event.action.value)
        self._connection.execute(INSERT_SQL, row)
        self._connection.commit()

    def get_last_event(self) -> Optional[Event]:
        row = self._connection.execute(SELECT_SQL).fetchone()
        if row is None:
            return None
        timestamp = datetime.fromisoformat(row[0])
        action = Action(row[1])
        return Event(timestamp, action)
