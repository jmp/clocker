from ..errors import NotClockedOutError
from ..event import InEvent
from ..repositories import EventRepository
from ..timestamp import Timestamp


class ClockInUseCase:
    def __init__(self, repository: EventRepository):
        self._repository = repository

    def clock_in(self, timestamp: Timestamp):
        last_event = self._repository.get_last_event()
        if isinstance(last_event, InEvent):
            raise NotClockedOutError()

        self._repository.insert_event(InEvent(timestamp))
