from clocker.event import ClockedIn, ClockedOut
from clocker.repositories import SQLiteEventRepository
from clocker.timestamp import Timestamp

from .helpers import InMemorySQLiteDatabase


def test_inserting_an_event_adds_a_new_row():
    database = InMemorySQLiteDatabase()
    event = ClockedIn(Timestamp("2022-05-22 11:30:00+03:00"))
    repository = SQLiteEventRepository(database.uri)

    repository.save(event)
    all_events = database.events()

    assert all_events == [("2022-05-22 08:30:00", "IN")]


def test_finding_last_event_sorts_by_timestamp():
    database = InMemorySQLiteDatabase()
    repository = SQLiteEventRepository(database.uri)
    database.insert_event("2022-05-01 16:30:45", "OUT")
    database.insert_event("2022-05-01 05:59:02", "IN")

    last_event = repository.find_last()

    assert last_event == ClockedOut(Timestamp("2022-05-01 16:30:45"))


def test_finding_last_event_returns_none_if_there_are_no_rows():
    database = InMemorySQLiteDatabase()
    repository = SQLiteEventRepository(database.uri)

    last_event = repository.find_last()

    assert last_event is None
