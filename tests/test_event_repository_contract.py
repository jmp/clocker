from clocker.event import ClockedIn, ClockedOut
from clocker.repositories import SQLiteEventRepository
from clocker.timestamp import Timestamp

from .helpers import InMemoryEventRepository


def test_get_last_event_returns_the_same_value_by_default():
    fake_repository = InMemoryEventRepository()
    sqlite_repository = SQLiteEventRepository(":memory:")

    fake_result = fake_repository.find_last()
    sqlite_result = sqlite_repository.find_last()

    assert fake_result is sqlite_result is None


def test_insert_event_inserts_a_single_clocked_in_event():
    fake_repository = InMemoryEventRepository()
    sqlite_repository = SQLiteEventRepository(":memory:")
    event = ClockedIn(Timestamp("2022-01-02 08:15"))

    fake_repository.save(event)
    sqlite_repository.save(event)

    fake_result = fake_repository.find_last()
    sqlite_result = sqlite_repository.find_last()
    expected_result = ClockedIn(Timestamp("2022-01-02 08:15"))

    assert fake_result == sqlite_result == expected_result


def test_insert_event_inserts_a_single_clocked_out_event():
    fake_repository = InMemoryEventRepository()
    sqlite_repository = SQLiteEventRepository(":memory:")
    event = ClockedOut(Timestamp("2022-01-02 15:30"))

    fake_repository.save(event)
    sqlite_repository.save(event)

    fake_result = fake_repository.find_last()
    sqlite_result = sqlite_repository.find_last()
    expected_result = ClockedOut(Timestamp("2022-01-02 15:30"))

    assert fake_result == sqlite_result == expected_result


def test_insert_multiple_events():
    fake_repository = InMemoryEventRepository()
    sqlite_repository = SQLiteEventRepository(":memory:")
    in_event = ClockedIn(Timestamp("2022-01-02 08:15"))
    out_event = ClockedOut(Timestamp("2022-01-02 16:30"))

    fake_repository.save(in_event)
    fake_repository.save(out_event)
    sqlite_repository.save(in_event)
    sqlite_repository.save(out_event)

    fake_result = fake_repository.find_last()
    sqlite_result = sqlite_repository.find_last()
    expected_result = ClockedOut(Timestamp("2022-01-02 16:30"))

    assert fake_result == sqlite_result == expected_result
