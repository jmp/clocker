from pytest import raises

from clocker.errors import NotClockedInError
from clocker.event import InEvent, OutEvent
from clocker.timestamp import Timestamp
from clocker.use_cases import ClockOutUseCase

from .helpers import InMemoryEventRepository


def test_clocking_out_records_an_out_event_if_clocked_in():
    last_event = InEvent(Timestamp("2022-05-22 08:15"))
    repository = InMemoryEventRepository(last_event)
    use_case = ClockOutUseCase(repository)

    use_case.clock_out(Timestamp("2022-05-22 19:50"))

    assert repository._inserted_event == OutEvent(Timestamp("2022-05-22 19:50"))


def test_clocking_out_raises_an_exception_if_there_are_no_events():
    repository = InMemoryEventRepository()
    use_case = ClockOutUseCase(repository)

    with raises(NotClockedInError):
        use_case.clock_out(Timestamp())


def test_clocking_out_raises_an_exception_if_already_clocked_out():
    last_event = OutEvent()
    repository = InMemoryEventRepository(last_event)
    use_case = ClockOutUseCase(repository)

    with raises(NotClockedInError):
        use_case.clock_out(Timestamp())
