from datetime import datetime

from clocker.event import EventType, Event
from clocker.event_repository import EventRepository


class FakeEventRepository(EventRepository):
    def __init__(self):
        self.inserted_event = None

    def insert_event(self, event: Event):
        self.inserted_event = event


class ClockInUseCase:
    def __init__(self, repository: EventRepository):
        self._repository = repository

    def clock_in(self, timestamp: datetime):
        event = Event(timestamp, EventType.IN)
        self._repository.insert_event(event)


def test_clocking_in_records_start_time():
    repository = FakeEventRepository()
    use_case = ClockInUseCase(repository)

    use_case.clock_in(datetime(2022, 5, 22, 19, 50))

    assert repository.inserted_event == Event(
        timestamp=datetime(2022, 5, 22, 19, 50),
        type=EventType.IN
    )
