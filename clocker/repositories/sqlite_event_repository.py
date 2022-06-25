from datetime import datetime
from sqlite3 import connect
from typing import Optional

from ..event import Event, EventType
from ..repositories import EventRepository


CREATE_SQL = """
    CREATE TABLE IF NOT EXISTS events (
        timestamp PRIMARY KEY NOT NULL,
        type NOT NULL
    )
"""
INSERT_SQL = "INSERT INTO events (timestamp, type) VALUES (?, ?)"
SELECT_SQL = "SELECT timestamp, type FROM events ORDER BY timestamp DESC LIMIT 1"


class SQLiteEventRepository(EventRepository):
    def __init__(self, path: str):
        self._connection = connect(path)
        self._connection.execute(CREATE_SQL)

    def insert_event(self, event: Event):
        row = (event.timestamp.isoformat(), event.type.value)
        self._connection.execute(INSERT_SQL, row)
        self._connection.commit()

    def get_last_event(self) -> Optional[Event]:
        row = self._connection.execute(SELECT_SQL).fetchone()
        if row is None:
            return None
        timestamp = datetime.fromisoformat(row[0])
        event_type = EventType(row[1])
        return Event(timestamp, event_type)
