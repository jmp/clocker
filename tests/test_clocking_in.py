from pytest import raises

from clocker.errors import NotClockedOutError
from clocker.event import InEvent, OutEvent
from clocker.timestamp import Timestamp
from clocker.use_cases import ClockInUseCase

from .helpers import InMemoryEventRepository


def test_clocking_in_records_an_in_event_if_there_are_no_events():
    repository = InMemoryEventRepository()
    use_case = ClockInUseCase(repository)

    use_case.clock_in(Timestamp("2022-05-22 08:30"))

    assert repository.find_last() == InEvent(Timestamp("2022-05-22 08:30"))


def test_clocking_in_records_an_in_event_if_clocked_out():
    repository = InMemoryEventRepository()
    repository.save(OutEvent(Timestamp("2022-05-22 16:45")))
    use_case = ClockInUseCase(repository)

    use_case.clock_in(Timestamp("2022-05-23 06:15"))

    assert repository.find_last() == InEvent(Timestamp("2022-05-23 06:15"))


def test_clocking_in_raises_an_exception_if_already_clocked_in():
    repository = InMemoryEventRepository()
    repository.save(InEvent())
    use_case = ClockInUseCase(repository)

    with raises(NotClockedOutError):
        use_case.clock_in(Timestamp())
