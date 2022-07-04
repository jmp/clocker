from pytest import raises

from datetime import datetime

from clocker.errors import NotClockedOutError
from clocker.event import Event
from clocker.action import Action
from clocker.use_cases import ClockInUseCase

from .mocks import MockEventRepository


def test_clocking_in_records_an_in_event():
    repository = MockEventRepository()
    use_case = ClockInUseCase(repository)

    use_case.clock_in(datetime(2022, 5, 22, 8, 30))

    assert repository.inserted_event == Event(datetime(2022, 5, 22, 8, 30), Action.IN)


def test_clocking_in_raises_an_exception_if_already_clocked_in():
    last_event = Event(datetime.now(), Action.IN)
    repository = MockEventRepository(last_event)
    use_case = ClockInUseCase(repository)

    with raises(NotClockedOutError):
        use_case.clock_in(datetime.now())
