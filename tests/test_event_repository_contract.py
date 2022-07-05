from clocker.event import Event
from clocker.action import Action
from clocker.repositories import SQLiteEventRepository
from clocker.timestamp import Timestamp

from .mocks import InMemoryEventRepository


def test_get_last_event_returns_the_same_value_by_default():
    mock_repository = InMemoryEventRepository()
    sqlite_repository = SQLiteEventRepository(":memory:")

    mock_result = mock_repository.get_last_event()
    sqlite_result = sqlite_repository.get_last_event()

    assert mock_result is sqlite_result is None


def test_insert_event_inserts_a_single_in_event():
    mock_repository = InMemoryEventRepository()
    sqlite_repository = SQLiteEventRepository(":memory:")
    event = Event(Timestamp("2022-01-02 08:15"), Action.IN)

    mock_repository.insert_event(event)
    sqlite_repository.insert_event(event)

    mock_result = mock_repository.get_last_event()
    sqlite_result = sqlite_repository.get_last_event()
    expected_result = Event(Timestamp("2022-01-02 08:15"), Action.IN)

    assert mock_result == sqlite_result == expected_result


def test_insert_event_inserts_a_single_out_event():
    mock_repository = InMemoryEventRepository()
    sqlite_repository = SQLiteEventRepository(":memory:")
    event = Event(Timestamp("2022-01-02 15:30"), Action.OUT)

    mock_repository.insert_event(event)
    sqlite_repository.insert_event(event)

    mock_result = mock_repository.get_last_event()
    sqlite_result = sqlite_repository.get_last_event()
    expected_result = Event(Timestamp("2022-01-02 15:30"), Action.OUT)

    assert mock_result == sqlite_result == expected_result


def test_insert_multiple_events():
    mock_repository = InMemoryEventRepository()
    sqlite_repository = SQLiteEventRepository(":memory:")
    in_event = Event(Timestamp("2022-01-02 08:15"), Action.IN)
    out_event = Event(Timestamp("2022-01-02 16:30"), Action.OUT)

    mock_repository.insert_event(in_event)
    mock_repository.insert_event(out_event)
    sqlite_repository.insert_event(in_event)
    sqlite_repository.insert_event(out_event)

    mock_result = mock_repository.get_last_event()
    sqlite_result = sqlite_repository.get_last_event()
    expected_result = Event(Timestamp("2022-01-02 16:30"), Action.OUT)

    assert mock_result == sqlite_result == expected_result
