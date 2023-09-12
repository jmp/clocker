from pytest import raises

from clocker.event import ClockedIn, ClockedOut
from clocker.timestamp import Timestamp
from clocker.use_cases import ClockOutUseCase, NotClockedInError

from .helpers import InMemoryEventRepository


def test_clocking_out_records_a_clocked_out_event_if_clocked_in():
    repository = InMemoryEventRepository()
    repository.save(ClockedIn(Timestamp("2022-05-22 08:15")))
    use_case = ClockOutUseCase(repository)

    use_case.clock_out(Timestamp("2022-05-22 19:50"))

    assert repository._inserted_event == ClockedOut(Timestamp("2022-05-22 19:50"))


def test_clocking_out_raises_an_exception_if_there_are_no_events():
    repository = InMemoryEventRepository()
    use_case = ClockOutUseCase(repository)

    with raises(NotClockedInError):
        use_case.clock_out(Timestamp())


def test_clocking_out_raises_an_exception_if_already_clocked_out():
    repository = InMemoryEventRepository()
    repository.save(ClockedOut())
    use_case = ClockOutUseCase(repository)

    with raises(NotClockedInError):
        use_case.clock_out(Timestamp())
