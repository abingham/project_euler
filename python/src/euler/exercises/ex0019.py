"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.

Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.

A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

from collections import OrderedDict
from itertools import count, cycle

from more_itertools import ilen


def is_leap_year(year):
    """Determine if `year` is a leap year.
    """
    if year % 100 == 0:
        return year % 400 == 0
    return year % 4 == 0


def days_of_week():
    """Inifinite sequences of day-of-week numbers, i.e. 1-7.

    Monday=1, Tuesday=2, etc.
    """
    return cycle(range(1, 8))


# Mapping of months to their number of days. February is special since it
# depends on leap-years. See `days_of_month()`.
NUM_DAYS_PER_MONTH = OrderedDict((
    ('jan', 31),
    ('feb', 0),
    ('mar', 31),
    ('apr', 30),
    ('may', 31),
    ('jun', 30),
    ('jul', 31),
    ('aug', 31),
    ('sep', 30),
    ('oct', 31),
    ('nov', 30),
    ('dec', 31)
))


def days_of_month(year):
    """An iterable of days-of-month for a given year.

    So first yields 1-31 for january, then 1-28 or 29 for Feburary, etc.
    """
    per_month = OrderedDict(NUM_DAYS_PER_MONTH)
    if is_leap_year(year):
        per_month['feb'] = 29
    else:
        per_month['feb'] = 28

    for month, num_days in per_month.items():
        yield from range(1, num_days + 1)


def all_days_of_month(to_year):
    """Sequence of all (day-of-month, year) tuples for the years 1900 to `to_year`.
    """
    return ((dom, year)
            for year in range(1900, to_year + 1)
            for dom in days_of_month(year))


def main():
    def count_day(day):
        dow, (dom, year) = day
        return dow == 7 and dom == 1 and year != 1900

    return ilen(
        filter(count_day,
               zip(days_of_week(),
                   all_days_of_month(2000))))
