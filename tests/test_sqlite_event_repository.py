from sqlite3 import connect

from clocker.event import InEvent, OutEvent
from clocker.repositories import SQLiteEventRepository
from clocker.timestamp import Timestamp


def test_inserting_an_event_adds_a_new_row(database):
    event = InEvent(Timestamp("2022-05-22 11:30:00+03:00"))
    repository = SQLiteEventRepository(database.file)

    repository.insert_event(event)

    assert database.events() == [("2022-05-22 08:30:00", "IN")]


def test_getting_last_event_fetches_the_last_row(database):
    repository = SQLiteEventRepository(database.file)

    database.insert_event("2022-05-01 05:59:02", "IN")
    database.insert_event("2022-05-01 16:30:45", "OUT")

    assert repository.get_last_event() == OutEvent(Timestamp("2022-05-01 16:30:45"))


def test_getting_last_event_returns_none_if_there_are_no_rows(database):
    repository = SQLiteEventRepository(database.file)

    last_event = repository.get_last_event()

    assert last_event is None
