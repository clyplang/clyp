import time as t
import datetime as dt

MINYEAR = dt.MINYEAR
MAXYEAR = dt.MAXYEAR
UTC = dt.UTC

#doc warning This module is very experimental and may change in the future. If stability is needed, please use "pyimport datetime" and use the python docs corresponding to your python version.

class TimeDelta:
    """
    A class representing a duration of time.
    """

    def __init__(self, days=0, seconds=0, microseconds=0):
        self._td = dt.timedelta(days=days, seconds=seconds, microseconds=microseconds)

    @classmethod
    def from_timedelta(cls, td: dt.timedelta):
        return cls(td.days, td.seconds, td.microseconds)

    @property
    def days(self):
        return self._td.days

    @property
    def seconds(self):
        return self._td.seconds

    @property
    def microseconds(self):
        return self._td.microseconds

    @staticmethod
    def min():
        """Get the minimum representable timedelta."""
        return dt.timedelta.min

    @staticmethod
    def max():
        """Get the maximum representable timedelta."""
        return dt.timedelta.max

    @staticmethod
    def resolution():
        """Get the smallest possible difference between non-equal timedelta objects."""
        return dt.timedelta.resolution

    def total_seconds(self):
        """
        Get the total duration in seconds.

        Returns:
            float: The total duration in seconds.
        """
        return self._td.total_seconds()

    def __add__(self, other):
        if isinstance(other, TimeDelta):
            return TimeDelta.from_timedelta(self._td + other._td)
        elif isinstance(other, dt.timedelta):
            return TimeDelta.from_timedelta(self._td + other)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, TimeDelta):
            return TimeDelta.from_timedelta(self._td - other._td)
        elif isinstance(other, dt.timedelta):
            return TimeDelta.from_timedelta(self._td - other)
        return NotImplemented

    def __neg__(self):
        return TimeDelta.from_timedelta(-self._td)

    def __eq__(self, other):
        if isinstance(other, TimeDelta):
            return self._td == other._td
        elif isinstance(other, dt.timedelta):
            return self._td == other
        return False

    def __repr__(self):
        return f"TimeDelta(days={self.days}, seconds={self.seconds}, microseconds={self.microseconds})"


class Time:
    """
    A class representing a time object.
    """

    def __init__(self, hour=0, minute=0, second=0, microsecond=0):
        self._time = dt.time(hour, minute, second, microsecond)

    @classmethod
    def now(cls):
        t = dt.datetime.now().time()
        return cls(
            t.hour,
            t.minute,
            t.second,
            t.microsecond,
        )

    def isoformat(self):
        return self._time.isoformat()

    @property
    def hour(self):
        return self._time.hour

    @property
    def minute(self):
        return self._time.minute

    @property
    def second(self):
        return self._time.second

    @property
    def microsecond(self):
        return self._time.microsecond

    def __repr__(self):
        return f"Time({self._time!r})"

    def __eq__(self, other):
        if isinstance(other, Time):
            return self._time == other._time
        return False


class Date:
    """
    A class representing a date object.
    """

    def __init__(self, year=1, month=1, day=1):
        self._date = dt.date(year, month, day)

    @classmethod
    def today(cls):
        d = dt.date.today()
        return cls(d.year, d.month, d.day)

    @classmethod
    def fromtimestamp(cls, timestamp):
        d = dt.date.fromtimestamp(timestamp)
        return cls(d.year, d.month, d.day)

    @classmethod
    def fromisoformat(cls, date_string):
        d = dt.date.fromisoformat(date_string)
        return cls(d.year, d.month, d.day)

    def isoformat(self):
        return self._date.isoformat()

    def weekday(self):
        return self._date.weekday()

    def toordinal(self):
        return self._date.toordinal()

    def strftime(self, format):
        return self._date.strftime(format)

    @classmethod
    def fromordinal(cls, ordinal):
        d = dt.date.fromordinal(ordinal)
        return cls(d.year, d.month, d.day)

    def replace(self, year=None, month=None, day=None):
        y = year if year is not None else self.year
        m = month if month is not None else self.month
        d = day if day is not None else self.day
        return Date(y, m, d)

    @property
    def year(self):
        return self._date.year

    @property
    def month(self):
        return self._date.month

    @property
    def day(self):
        return self._date.day

    def __repr__(self):
        return f"Date({self._date!r})"

    def __eq__(self, other):
        if isinstance(other, Date):
            return self._date == other._date
        return False


class DateTime:
    """
    A single object containing information of a specific point in time. DateTime assumes the Gregorian calendar.
    """

    def __init__(
        self,
        year,
        month,
        day,
        hour=0,
        minute=0,
        second=0,
        microsecond=0,
        tzinfo=None,
    ):
        self._dt = dt.datetime(
            year, month, day, hour, minute, second, microsecond, tzinfo
        )

    @classmethod
    def now(cls):
        d = dt.datetime.now()
        return cls(
            d.year,
            d.month,
            d.day,
            d.hour,
            d.minute,
            d.second,
            d.microsecond,
            d.tzinfo,
        )

    @classmethod
    def utcnow(cls):
        d = dt.datetime.utcnow()
        return cls(
            d.year,
            d.month,
            d.day,
            d.hour,
            d.minute,
            d.second,
            d.microsecond,
            d.tzinfo,
        )

    @classmethod
    def fromtimestamp(cls, timestamp):
        d = dt.datetime.fromtimestamp(timestamp)
        return cls(
            d.year,
            d.month,
            d.day,
            d.hour,
            d.minute,
            d.second,
            d.microsecond,
            d.tzinfo,
        )

    def isoformat(self):
        return self._dt.isoformat()

    @property
    def year(self):
        return self._dt.year

    @property
    def month(self):
        return self._dt.month

    @property
    def day(self):
        return self._dt.day

    @property
    def hour(self):
        return self._dt.hour

    @property
    def minute(self):
        return self._dt.minute

    @property
    def second(self):
        return self._dt.second

    @property
    def microsecond(self):
        return self._dt.microsecond

    @property
    def tzinfo(self):
        return self._dt.tzinfo

    def __repr__(self):
        return f"DateTime({self._dt!r})"

    def __eq__(self, other):
        if isinstance(other, DateTime):
            return self._dt == other._dt
        return False


class Timezone:
    """
    A class representing a timezone.
    """

    def __init__(self, name: str, offset: dt.timedelta):
        self.name = name
        self.offset = offset

    def utcoffset(self, dt: DateTime) -> dt.timedelta:
        """
        Get the UTC offset for a specific DateTime.

        Args:
            dt (DateTime): The DateTime object to get the offset for.

        Returns:
            timedelta: The UTC offset.
        """
        return self.offset

    def dst(self, dt_obj: DateTime) -> dt.timedelta:
        """
        Get the daylight saving time offset for a specific DateTime.

        Args:
            dt_obj (DateTime): The DateTime object to get the DST offset for.

        Returns:
            timedelta: The DST offset.
        """
        return dt.timedelta(0)

    def __repr__(self):
        return f"Timezone(name={self.name}, offset={self.offset})"


def sleep(seconds: float) -> None:
    """
    Suspend execution of the calling thread for the given number of seconds.

    Args:
        seconds (float): The number of seconds to pause execution.
    """
    t.sleep(seconds)


def time() -> float:
    """
    Get the current time in seconds since the Unix epoch.

    Returns:
        float: The current time in seconds since January 1, 1970.
    """
    return t.time()


def monotonic() -> float:
    """
    Get the value of a monotonic clock, which cannot go backwards.

    Returns:
        float: The current value of a monotonic clock in fractional seconds.
    """
    return t.monotonic()


def perf_counter() -> float:
    """
    Get the value of a high-resolution performance counter.

    Returns:
        float: The current value of the performance counter in fractional seconds.
    """
    return t.perf_counter()


def strftime(format: str, timestamp: float) -> str:
    """
    Format a timestamp into a string according to the specified format.

    Args:
        format (str): The format string compatible with strftime.
        timestamp (float): The time to format, in seconds since the epoch.

    Returns:
        str: The formatted time string.
    """
    return t.strftime(format, t.localtime(timestamp))


def strptime(date_string: str, format: str) -> t.struct_time:
    """
    Parse a string representing a time according to a format.

    Args:
        date_string (str): The string to parse.
        format (str): The format string compatible with strptime.

    Returns:
        struct_time: The parsed time as a struct_time object.
    """
    return t.strptime(date_string, format)


def now() -> float:
    """
    Get the current local date and time as a timestamp (float).

    Returns:
        float: The current local date and time as a timestamp.
    """
    return dt.datetime.now().timestamp()
def format(timestamp: float) -> str:
    """
    Format a timestamp into a human-readable string.

    Args:
        timestamp (float): The timestamp to format.

    Returns:
        str: The formatted time string.
    """
    try:
        return dt.datetime.fromtimestamp(float(timestamp), dt.UTC).strftime('%Y-%m-%d %H:%M:%S')
    except Exception as e:
        raise Exception(f"Invalid timestamp: {timestamp}") from e


def today() -> dt.date:
    """
    Get the current local date.

    Returns:
        date: The current local date.
    """
    return dt.date.today()


def fromtimestamp(timestamp: float) -> DateTime:
    """
    Create a DateTime object from a Unix timestamp.

    Args:
        timestamp (float): The Unix timestamp.

    Returns:
        DateTime: The corresponding DateTime object.
    """
    return DateTime.fromtimestamp(timestamp)


def utcnow() -> DateTime:
    """
    Get the current UTC date and time.

    Returns:
        DateTime: The current UTC date and time.
    """
    return DateTime.utcnow()


def isoformat(dt_obj: DateTime) -> str:
    """
    Convert a DateTime object to an ISO 8601 formatted string.

    Args:
        dt_obj (DateTime): The DateTime object to convert.

    Returns:
        str: The ISO 8601 formatted string.
    """
    return dt_obj.isoformat()
