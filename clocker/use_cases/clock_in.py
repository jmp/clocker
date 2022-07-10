from ..event import InEvent
from ..repositories import EventRepository
from ..timestamp import Timestamp


class ClockInUseCase:
    def __init__(self, repository: EventRepository):
        self._repository = repository

    def clock_in(self, timestamp: Timestamp):
        last_event = self._repository.find_last()
        if isinstance(last_event, InEvent):
            raise NotClockedOutError()

        self._repository.save(InEvent(timestamp))


class NotClockedOutError(RuntimeError):
    pass
