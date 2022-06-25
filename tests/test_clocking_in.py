from pytest import raises

from datetime import datetime

from clocker.errors import AlreadyClockedInError
from clocker.event import EventType, Event
from clocker.use_cases import ClockInUseCase

from .fake_event_repository import FakeEventRepository


def test_clocking_in_records_start_time():
    repository = FakeEventRepository()
    use_case = ClockInUseCase(repository)

    use_case.clock_in(datetime(2022, 5, 22, 19, 50))

    assert repository.inserted_event == Event(
        timestamp=datetime(2022, 5, 22, 19, 50),
        type=EventType.IN
    )


def test_clocking_in_raises_an_exception_if_already_clocked_in():
    last_event = Event(datetime(2022, 5, 22, 19, 50), EventType.IN)
    repository = FakeEventRepository(last_event)
    use_case = ClockInUseCase(repository)

    with raises(AlreadyClockedInError):
        use_case.clock_in(datetime(2022, 5, 22, 19, 51))
