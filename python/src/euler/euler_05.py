"""2520 is the smallest number that can be divided by each of the numbers from
1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?

"""

from itertools import count


def minimize_divisors(divisors):
    """Reduce a set of divisors to a minimal set.

    This removes any element in `divisor` which cleanly divides into any other
    member.

    Note that, for the narrow case of this exercise, this method is overkill.
    We always deal with all integers from 1 to some value, in which case this
    function could just return the upper half of that range. But for the more
    general case of an arbitrary set of divisors, this seems to work.

    Args:
        divisors: An iterable of integers.

    Returns: An iterable of integers with redundant divisors removed.

    """
    divisors = sorted(set(divisors))
    return (d
            for index, d
            in enumerate(divisors)
            if not any(bd % d == 0 for bd in divisors[index + 1:]))


def min_divided_by(divisors):
    divisors = list(minimize_divisors(divisors))
    divisors.sort(reverse=True)
    return next(
        val
        for val in count(start=divisors[0], step=divisors[0])
        if all(val % d == 0 for d in divisors))


def main():
    return min_divided_by(range(1, 21))
