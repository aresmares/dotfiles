from collections.abc import (
    Hashable,
    Sequence,
)
from datetime import (
    datetime,
    timedelta,
    tzinfo,
)
from typing import overload

import numpy as np
from pandas import (
    DataFrame,
    Index,
    Timedelta,
    TimedeltaIndex,
    Timestamp,
)
from pandas.core.indexes.accessors import DatetimeIndexProperties
from pandas.core.indexes.datetimelike import DatetimeTimedeltaMixin
from pandas.core.series import (
    TimedeltaSeries,
    TimestampSeries,
)
from typing_extensions import Self

from pandas._typing import (
    AxesData,
    DateAndDatetimeLike,
    Dtype,
    Frequency,
    IntervalClosedType,
    TimeUnit,
    TimeZones,
)

from pandas.core.dtypes.dtypes import DatetimeTZDtype

from pandas.tseries.offsets import BaseOffset

class DatetimeIndex(DatetimeTimedeltaMixin[Timestamp], DatetimeIndexProperties):
    def __init__(
        self,
        data: AxesData,
        freq: Frequency = ...,
        tz: TimeZones = ...,
        ambiguous: str = ...,
        dayfirst: bool = ...,
        yearfirst: bool = ...,
        dtype: Dtype = ...,
        copy: bool = ...,
        name: Hashable = ...,
    ) -> None: ...
    def __array__(self, dtype=...) -> np.ndarray: ...
    def __reduce__(self): ...
    # various ignores needed for mypy, as we do want to restrict what can be used in
    # arithmetic for these types
    @overload
    def __add__(self, other: TimedeltaSeries) -> TimestampSeries: ...
    @overload
    def __add__(
        self, other: timedelta | Timedelta | TimedeltaIndex | BaseOffset
    ) -> DatetimeIndex: ...
    @overload
    def __sub__(self, other: TimedeltaSeries) -> TimestampSeries: ...
    @overload
    def __sub__(
        self, other: timedelta | Timedelta | TimedeltaIndex | BaseOffset
    ) -> DatetimeIndex: ...
    @overload
    def __sub__(
        self, other: datetime | Timestamp | DatetimeIndex
    ) -> TimedeltaIndex: ...
    def to_series(self, index=..., name: Hashable = ...) -> TimestampSeries: ...
    def snap(self, freq: str = ...): ...
    def slice_indexer(self, start=..., end=..., step=...): ...
    def searchsorted(self, value, side: str = ..., sorter=...): ...
    @property
    def inferred_type(self) -> str: ...
    def indexer_at_time(self, time, asof: bool = ...): ...
    def indexer_between_time(
        self, start_time, end_time, include_start: bool = ..., include_end: bool = ...
    ): ...
    def to_julian_date(self) -> Index[float]:
        """
Convert Datetime Array to float64 ndarray of Julian Dates.
0 Julian date is noon January 1, 4713 BC.
https://en.wikipedia.org/wiki/Julian_day
        """
        pass
    def isocalendar(self) -> DataFrame:
        """
Calculate year, week, and day according to the ISO 8601 standard.

Returns
-------
DataFrame
    With columns year, week and day.

See Also
--------
Timestamp.isocalendar : Function return a 3-tuple containing ISO year,
    week number, and weekday for the given Timestamp object.
datetime.date.isocalendar : Return a named tuple object with
    three components: year, week and weekday.

Examples
--------
>>> idx = pd.date_range(start='2019-12-29', freq='D', periods=4)
>>> idx.isocalendar()
            year  week  day
2019-12-29  2019    52    7
2019-12-30  2020     1    1
2019-12-31  2020     1    2
2020-01-01  2020     1    3
>>> idx.isocalendar().week
2019-12-29    52
2019-12-30     1
2019-12-31     1
2020-01-01     1
Freq: D, Name: week, dtype: UInt32
        """
        pass
    @property
    def tzinfo(self) -> tzinfo | None: ...
    @property
    def dtype(self) -> np.dtype | DatetimeTZDtype: ...
    def shift(self, periods: int = ..., freq=...) -> Self: ...

def date_range(
    start: str | DateAndDatetimeLike | None = ...,
    end: str | DateAndDatetimeLike | None = ...,
    periods: int | None = ...,
    freq: str | timedelta | Timedelta | BaseOffset = ...,
    tz: TimeZones = ...,
    normalize: bool = ...,
    name: Hashable | None = ...,
    inclusive: IntervalClosedType = ...,
    unit: TimeUnit | None = ...,
) -> DatetimeIndex: ...
@overload
def bdate_range(
    start: str | DateAndDatetimeLike | None = ...,
    end: str | DateAndDatetimeLike | None = ...,
    periods: int | None = ...,
    freq: str | timedelta | Timedelta | BaseOffset = ...,
    tz: TimeZones = ...,
    normalize: bool = ...,
    name: Hashable | None = ...,
    weekmask: str | None = ...,
    holidays: None = ...,
    inclusive: IntervalClosedType = ...,
) -> DatetimeIndex: ...
@overload
def bdate_range(
    start: str | DateAndDatetimeLike | None = ...,
    end: str | DateAndDatetimeLike | None = ...,
    periods: int | None = ...,
    *,
    freq: str | timedelta | Timedelta | BaseOffset,
    tz: TimeZones = ...,
    normalize: bool = ...,
    name: Hashable | None = ...,
    weekmask: str | None = ...,
    holidays: Sequence[str | DateAndDatetimeLike],
    inclusive: IntervalClosedType = ...,
) -> DatetimeIndex: ...
