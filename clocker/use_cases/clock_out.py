from ..event import ClockedOut
from ..repositories import EventRepository
from ..timestamp import Timestamp


class ClockOutUseCase:
    def __init__(self, repository: EventRepository):
        self._repository = repository

    def clock_out(self, timestamp: Timestamp):
        last_event = self._repository.find_last()
        if last_event is None or isinstance(last_event, ClockedOut):
            raise NotClockedInError()

        self._repository.save(ClockedOut(timestamp))


class NotClockedInError(RuntimeError):
    pass
