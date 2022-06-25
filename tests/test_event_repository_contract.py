from datetime import datetime

from clocker.event import Event, EventType
from clocker.repositories import SQLiteEventRepository

from .mocks import MockEventRepository


def test_get_last_event_returns_the_same_value_by_default():
    mock_repository = MockEventRepository()
    sqlite_repository = SQLiteEventRepository(":memory:")

    mock_result = mock_repository.get_last_event()
    sqlite_result = sqlite_repository.get_last_event()

    assert mock_result == sqlite_result


def test_insert_event_inserts_a_single_in_event():
    mock_repository = MockEventRepository()
    sqlite_repository = SQLiteEventRepository(":memory:")
    event = Event(datetime(2022, 1, 2, 8, 15), EventType.IN)

    mock_repository.insert_event(event)
    sqlite_repository.insert_event(event)

    mock_result = mock_repository.get_last_event()
    sqlite_result = sqlite_repository.get_last_event()

    assert mock_result == sqlite_result


def test_insert_event_inserts_a_single_out_event():
    mock_repository = MockEventRepository()
    sqlite_repository = SQLiteEventRepository(":memory:")
    event = Event(datetime(2022, 1, 2, 15, 30), EventType.OUT)

    mock_repository.insert_event(event)
    sqlite_repository.insert_event(event)

    mock_result = mock_repository.get_last_event()
    sqlite_result = sqlite_repository.get_last_event()

    assert mock_result == sqlite_result


def test_insert_multiple_events():
    mock_repository = MockEventRepository()
    sqlite_repository = SQLiteEventRepository(":memory:")
    in_event = Event(datetime(2022, 1, 2, 8, 15), EventType.IN)
    out_event = Event(datetime(2022, 1, 2, 16, 30), EventType.OUT)

    mock_repository.insert_event(in_event)
    mock_repository.insert_event(out_event)
    sqlite_repository.insert_event(in_event)
    sqlite_repository.insert_event(out_event)

    mock_result = mock_repository.get_last_event()
    sqlite_result = sqlite_repository.get_last_event()

    assert mock_result == sqlite_result
