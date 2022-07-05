from pytest import raises

from clocker.errors import NotClockedInError
from clocker.event import Event
from clocker.action import Action
from clocker.timestamp import Timestamp
from clocker.use_cases import ClockOutUseCase

from .mocks import InMemoryEventRepository


def test_clocking_out_records_an_out_event_if_clocked_in():
    last_event = Event(Timestamp("2022-05-22 08:15"), Action.IN)
    repository = InMemoryEventRepository(last_event)
    use_case = ClockOutUseCase(repository)

    use_case.clock_out(Timestamp("2022-05-22 19:50"))

    assert repository.inserted_event == Event(Timestamp("2022-05-22 19:50"), Action.OUT)


def test_clocking_out_raises_an_exception_if_there_are_no_events():
    repository = InMemoryEventRepository()
    use_case = ClockOutUseCase(repository)

    with raises(NotClockedInError):
        use_case.clock_out(Timestamp())


def test_clocking_out_raises_an_exception_if_already_clocked_out():
    last_event = Event(Timestamp(), Action.OUT)
    repository = InMemoryEventRepository(last_event)
    use_case = ClockOutUseCase(repository)

    with raises(NotClockedInError):
        use_case.clock_out(Timestamp())
