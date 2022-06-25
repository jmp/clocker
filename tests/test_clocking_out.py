from pytest import raises

from datetime import datetime

from clocker.errors import NotClockedInError
from clocker.event import EventType, Event
from clocker.use_cases import ClockOutUseCase

from .fake_event_repository import FakeEventRepository


def test_clocking_out_records_end_time():
    last_event = Event(datetime(2022, 5, 22, 8, 15), EventType.IN)
    repository = FakeEventRepository(last_event)
    use_case = ClockOutUseCase(repository)

    use_case.clock_out(datetime(2022, 5, 22, 19, 50))

    assert repository.inserted_event == Event(
        timestamp=datetime(2022, 5, 22, 19, 50),
        type=EventType.OUT
    )


def test_clocking_out_raises_an_exception_if_not_clocked_in():
    repository = FakeEventRepository()
    use_case = ClockOutUseCase(repository)

    with raises(NotClockedInError):
        use_case.clock_out(datetime(2022, 5, 22, 19, 51))
