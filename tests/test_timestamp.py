from datetime import datetime, timedelta, timezone

from clocker.timestamp import Timestamp


def test_timestamp_without_parameters_uses_current_time_in_utc():
    before = datetime.now(timezone.utc) - timedelta(seconds=1)
    timestamp = Timestamp()
    after = datetime.now(timezone.utc) + timedelta(seconds=1)

    actual = datetime.fromisoformat(str(timestamp)).replace(tzinfo=timezone.utc)

    assert before < actual < after


def test_timestamp_without_timezone_is_interpreted_as_utc():
    timestamp = Timestamp("2022-07-05 17:34:13")

    assert str(timestamp) == "2022-07-05 17:34:13"


def test_timestamp_with_timezone_is_converted_to_utc():
    timestamp = Timestamp("2022-07-05 20:38:50+03:00")

    assert str(timestamp) == "2022-07-05 17:38:50"


def test_same_timestamps_with_different_timezones_are_equal():
    timestamp1 = Timestamp("2022-07-06 01:00:00+00:00")
    timestamp2 = Timestamp("2022-07-06 03:00:00+02:00")

    assert timestamp1 == timestamp2
