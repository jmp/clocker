from datetime import datetime, timezone
from sqlite3 import connect

from clocker.event import Event, EventType
from clocker.repositories.sqlite_event_repository import SQLiteEventRepository


SHARED_SQLITE_DATABASE = "file::memory:?cache=shared"


def test_inserting_an_event_adds_a_new_row():
    event = Event(datetime(2022, 5, 22, 8, 30, tzinfo=timezone.utc), EventType.IN)
    repository = SQLiteEventRepository(SHARED_SQLITE_DATABASE)
    repository.insert_event(event)

    with connect(SHARED_SQLITE_DATABASE) as connection:
        row = connection.execute("SELECT * FROM events").fetchone()
        assert row == ("2022-05-22 08:30:00+00:00", 0)


def test_getting_last_event_fetches_the_last_row():
    repository = SQLiteEventRepository(SHARED_SQLITE_DATABASE)

    with connect(SHARED_SQLITE_DATABASE) as connection:
        connection.execute(
            "INSERT INTO events (timestamp, type) VALUES (?, ?), (?, ?)",
            (
                "2022-05-01 05:59:02+00:00", 0,
                "2022-05-01 16:30:45+00:00", 1,
            ),
        )
        connection.commit()

    last_event = repository.get_last_event()
    expected_event = Event(datetime(2022, 5, 1, 16, 30, 45, tzinfo=timezone.utc), EventType.OUT)

    assert last_event == expected_event


def test_getting_last_event_returns_none_there_are_no_rows():
    repository = SQLiteEventRepository(SHARED_SQLITE_DATABASE)

    last_event = repository.get_last_event()

    assert last_event is None
