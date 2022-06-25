from typing import Optional

from datetime import datetime

from clocker.event import EventType, Event
from clocker.event_repository import EventRepository
from clocker.use_cases.clock_out import ClockOutUseCase


class FakeEventRepository(EventRepository):
    def __init__(self):
        self.inserted_event = None

    def insert_event(self, event: Event):
        self.inserted_event = event

    def get_last_event(self) -> Optional[Event]:
        return self.inserted_event


def test_clocking_out_records_end_time():
    repository = FakeEventRepository()
    use_case = ClockOutUseCase(repository)

    use_case.clock_out(datetime(2022, 5, 22, 19, 50))

    assert repository.inserted_event == Event(
        timestamp=datetime(2022, 5, 22, 19, 50),
        type=EventType.OUT
    )
