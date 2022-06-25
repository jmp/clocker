from datetime import datetime
from sqlite3 import connect
from typing import Optional

from ..event import Event, EventType
from ..repositories import EventRepository


class SQLiteEventRepository(EventRepository):
    def __init__(self, path: str):
        self._connection = connect(path)
        self._connection.execute(
                """
                CREATE TABLE IF NOT EXISTS events (
                    timestamp PRIMARY KEY NOT NULL,
                    type NOT NULL
                )
                """
            )

    def insert_event(self, event: Event):
        self._connection.execute(
            "INSERT INTO events (timestamp, type) VALUES (?, ?)",
            (event.timestamp, event.type.value),
        )
        self._connection.commit()

    def get_last_event(self) -> Optional[Event]:
        row = self._connection.execute("SELECT timestamp, type FROM events ORDER BY timestamp DESC LIMIT 1").fetchone()
        if row is None:
            return None
        timestamp = datetime.fromisoformat(row[0])
        event_type = EventType(row[1])
        return Event(timestamp, event_type)
