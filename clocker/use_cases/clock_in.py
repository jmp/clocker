from ..event import ClockedIn
from ..repositories import EventRepository
from ..timestamp import Timestamp


class ClockInUseCase:
    def __init__(self, repository: EventRepository):
        self._repository = repository

    def clock_in(self, timestamp: Timestamp):
        last_event = self._repository.find_last()
        if isinstance(last_event, ClockedIn):
            raise NotClockedOutError()

        self._repository.save(ClockedIn(timestamp))


class NotClockedOutError(RuntimeError):
    pass
