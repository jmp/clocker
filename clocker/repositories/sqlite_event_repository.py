from sqlite3 import connect
from typing import Optional

from ..event import Event, InEvent, OutEvent
from ..action import Action
from ..repositories import EventRepository
from ..timestamp import Timestamp

CREATE_SQL = """
    CREATE TABLE IF NOT EXISTS events (
        timestamp PRIMARY KEY NOT NULL,
        action NOT NULL
    )
"""
INSERT_SQL = "INSERT INTO events (timestamp, action) VALUES (?, ?)"
SELECT_SQL = "SELECT timestamp, action FROM events ORDER BY timestamp DESC, rowid LIMIT 1"


class SQLiteEventRepository(EventRepository):
    def __init__(self, path: str):
        self._connection = connect(path)
        self._connection.execute(CREATE_SQL)

    def save(self, event: Event):
        self._connection.execute(INSERT_SQL, (str(event.timestamp), event.action.value))
        self._connection.commit()

    def find_last(self) -> Optional[Event]:
        row = self._connection.execute(SELECT_SQL).fetchone()
        if row is None:
            return None
        timestamp = Timestamp(row[0])
        action = Action(row[1])
        if action == Action.IN:
            return InEvent(timestamp)
        return OutEvent(timestamp)
