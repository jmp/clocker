from pytest import raises

from datetime import datetime

from clocker.errors import AlreadyClockedInError
from clocker.event import EventType, Event
from clocker.use_cases import ClockInUseCase

from .mocks import MockEventRepository


def test_clocking_in_records_an_in_event():
    repository = MockEventRepository()
    use_case = ClockInUseCase(repository)

    use_case.clock_in(datetime(2022, 5, 22, 8, 30))

    assert repository.inserted_event == Event(datetime(2022, 5, 22, 8, 30), EventType.IN)


def test_clocking_in_raises_an_exception_if_already_clocked_in():
    last_event = Event(datetime(2022, 5, 22, 8, 30), EventType.IN)
    repository = MockEventRepository(last_event)
    use_case = ClockInUseCase(repository)

    with raises(AlreadyClockedInError):
        use_case.clock_in(datetime(2022, 5, 22, 8, 31))
