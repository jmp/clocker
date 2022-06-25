from pytest import raises

from datetime import datetime

from clocker.errors import AlreadyClockedOutError
from clocker.event import EventType, Event
from clocker.use_cases import ClockOutUseCase

from .mocks import MockEventRepository


def test_clocking_out_records_an_out_event():
    last_event = Event(datetime(2022, 5, 22, 8, 15), EventType.IN)
    repository = MockEventRepository(last_event)
    use_case = ClockOutUseCase(repository)

    use_case.clock_out(datetime(2022, 5, 22, 19, 50))

    assert repository.inserted_event == Event(
        timestamp=datetime(2022, 5, 22, 19, 50),
        type=EventType.OUT
    )


def test_clocking_out_raises_an_exception_if_there_are_no_events():
    repository = MockEventRepository()
    use_case = ClockOutUseCase(repository)

    with raises(AlreadyClockedOutError):
        use_case.clock_out(datetime(2022, 5, 22, 19, 51))


def test_clocking_out_raises_an_exception_if_already_clocked_out():
    last_event = Event(datetime(2022, 5, 22, 8, 15), EventType.OUT)
    repository = MockEventRepository(last_event)
    use_case = ClockOutUseCase(repository)

    with raises(AlreadyClockedOutError):
        use_case.clock_out(datetime(2022, 5, 22, 19, 51))
