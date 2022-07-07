from sqlite3 import connect

from clocker.event import InEvent, OutEvent
from clocker.repositories import SQLiteEventRepository
from clocker.timestamp import Timestamp


def test_inserting_an_event_adds_a_new_row():
    db_file = "file:insert?cache=shared&mode=memory"
    event = InEvent(Timestamp("2022-05-22 11:30:00+03:00"))
    repository = SQLiteEventRepository(db_file)
    repository.insert_event(event)

    with connect(db_file, uri=True) as connection:
        row = connection.execute("SELECT * FROM events").fetchone()
        assert row == ("2022-05-22 08:30:00", "IN")


def test_getting_last_event_fetches_the_last_row():
    db_file = "file:getlast?cache=shared&mode=memory"
    repository = SQLiteEventRepository(db_file)

    with connect(db_file, uri=True) as connection:
        connection.execute(
            "INSERT INTO events (timestamp, action) VALUES (?, ?), (?, ?)",
            (
                "2022-05-01 05:59:02", "IN",
                "2022-05-01 16:30:45", "OUT",
            ),
        )
        connection.commit()

    last_event = repository.get_last_event()
    expected_event = OutEvent(Timestamp("2022-05-01 16:30:45"))

    assert last_event == expected_event


def test_getting_last_event_returns_none_if_there_are_no_rows():
    repository = SQLiteEventRepository(":memory:")

    last_event = repository.get_last_event()

    assert last_event is None
