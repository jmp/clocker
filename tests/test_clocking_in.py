from pytest import raises

from clocker.errors import NotClockedOutError
from clocker.event import Event
from clocker.action import Action
from clocker.timestamp import Timestamp
from clocker.use_cases import ClockInUseCase

from .mocks import InMemoryEventRepository


def test_clocking_in_records_an_in_event_if_there_are_no_events():
    repository = InMemoryEventRepository()
    use_case = ClockInUseCase(repository)

    use_case.clock_in(Timestamp("2022-05-22 08:30"))

    assert repository.inserted_event == Event(Timestamp("2022-05-22 08:30"), Action.IN)


def test_clocking_in_records_an_in_event_if_clocked_out():
    last_event = Event(Timestamp("2022-05-22 16:45"), Action.OUT)
    repository = InMemoryEventRepository(last_event)
    use_case = ClockInUseCase(repository)

    use_case.clock_in(Timestamp("2022-05-23 06:15"))

    assert repository.inserted_event == Event(Timestamp("2022-05-23 06:15"), Action.IN)


def test_clocking_in_raises_an_exception_if_already_clocked_in():
    last_event = Event(Timestamp(), Action.IN)
    repository = InMemoryEventRepository(last_event)
    use_case = ClockInUseCase(repository)

    with raises(NotClockedOutError):
        use_case.clock_in(Timestamp())
