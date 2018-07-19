"""Surprisingly there are only three numbers that can be written as the sum of
fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 94 + 44 + 74 + 44

As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers
of their digits. import euler_util
"""

from itertools import takewhile

from euler.lib.util import digits


def sums_of_powers_of_digits(power):
    """Iterable of all integers which are sums of their digits raised to `power`.
    """
    # TODO: This is sloppy. Need better assurance that this max_val is
    # reasonable. Right now it's a guesstimate.
    max_val = 10 ** (power + 1)
    return (
        n
        for n
        in range(2, max_val + 1)
        if n == sum(d ** power for d in digits(n)))


def sum_of_values(power):
    return sum(sums_of_powers_of_digits(power))


def main():
    return sum_of_values(5)
