from datetime import datetime

from clocker.event import EventType, Event
from clocker.use_cases.clock_out import ClockOutUseCase

from .fake_event_repository import FakeEventRepository


def test_clocking_out_records_end_time():
    repository = FakeEventRepository()
    use_case = ClockOutUseCase(repository)

    use_case.clock_out(datetime(2022, 5, 22, 19, 50))

    assert repository.inserted_event == Event(
        timestamp=datetime(2022, 5, 22, 19, 50),
        type=EventType.OUT
    )
