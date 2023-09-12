from clocker.event import ClockedIn, ClockedOut
from clocker.repositories import SQLiteEventRepository
from clocker.timestamp import Timestamp
from clocker.use_cases import ClockInUseCase, ClockOutUseCase


def test_clocking_in_with_real_database():
    repository = SQLiteEventRepository(":memory:")
    use_case = ClockInUseCase(repository)

    use_case.clock_in(Timestamp("2022-06-08 22:48:33+03:00"))

    last_event = repository.find_last()

    assert last_event == ClockedIn(Timestamp("2022-06-08 19:48:33"))


def test_clocking_out_with_real_database():
    repository = SQLiteEventRepository(":memory:")
    repository.save(ClockedIn(Timestamp("2022-06-08 06:30:24")))
    use_case = ClockOutUseCase(repository)

    use_case.clock_out(Timestamp("2022-06-08 16:02:18+03:00"))

    last_event = repository.find_last()

    assert last_event == ClockedOut(Timestamp("2022-06-08 13:02:18"))
