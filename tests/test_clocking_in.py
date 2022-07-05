from pytest import raises

from datetime import datetime

from clocker.errors import NotClockedOutError
from clocker.event import Event
from clocker.action import Action
from clocker.use_cases import ClockInUseCase

from .mocks import InMemoryEventRepository


def test_clocking_in_records_an_in_event_if_there_are_no_events():
    repository = InMemoryEventRepository()
    use_case = ClockInUseCase(repository)

    use_case.clock_in(datetime(2022, 5, 22, 8, 30))

    assert repository.inserted_event == Event(datetime(2022, 5, 22, 8, 30), Action.IN)


def test_clocking_in_records_an_in_event_if_clocked_out():
    last_event = Event(datetime(2022, 5, 22, 16, 45), Action.OUT)
    repository = InMemoryEventRepository(last_event)
    use_case = ClockInUseCase(repository)

    use_case.clock_in(datetime(2022, 5, 23, 6, 15))

    assert repository.inserted_event == Event(datetime(2022, 5, 23, 6, 15), Action.IN)


def test_clocking_in_raises_an_exception_if_already_clocked_in():
    last_event = Event(datetime.now(), Action.IN)
    repository = InMemoryEventRepository(last_event)
    use_case = ClockInUseCase(repository)

    with raises(NotClockedOutError):
        use_case.clock_in(datetime.now())
