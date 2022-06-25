from typing import Optional

from pytest import raises

from datetime import datetime

from clocker.errors import AlreadyClockedInError
from clocker.event import EventType, Event
from clocker.event_repository import EventRepository
from clocker.use_cases import ClockInUseCase


class FakeEventRepository(EventRepository):
    def __init__(self):
        self.inserted_event = None

    def insert_event(self, event: Event):
        self.inserted_event = event

    def get_last_event(self) -> Optional[Event]:
        return self.inserted_event


def test_clocking_in_records_start_time():
    repository = FakeEventRepository()
    use_case = ClockInUseCase(repository)

    use_case.clock_in(datetime(2022, 5, 22, 19, 50))

    assert repository.inserted_event == Event(
        timestamp=datetime(2022, 5, 22, 19, 50),
        type=EventType.IN
    )


def test_clocking_in_raises_an_exception_if_already_clocked_in():
    repository = FakeEventRepository()
    use_case = ClockInUseCase(repository)

    use_case.clock_in(datetime(2022, 5, 22, 19, 50))

    with raises(AlreadyClockedInError):
        use_case.clock_in(datetime(2022, 5, 22, 19, 51))
