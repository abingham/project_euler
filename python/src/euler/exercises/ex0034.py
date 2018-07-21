"""145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of
their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

from math import factorial
from euler.lib.util import digits


def factorial_sum(n):
    return sum(map(factorial, digits(n)))


def is_curious(n):
    if n < 3:
        return False

    return n == factorial_sum(n)


def curious():
    # TODO: I didn't arrive at the 50000 limit through any reasoning, just
    # guesswork. How can we determine where the limit is?
    return filter(is_curious, range(50000))


def main():
    return sum(curious())
