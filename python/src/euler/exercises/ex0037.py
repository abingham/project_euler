"""The number 3797 has an interesting property. Being prime itself, it is
possible to continuously remove digits from left to right, and remain prime at
each stage: 3797, 797, 97, and 7. Similarly we can work from right to left:
3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to
right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

from itertools import chain, dropwhile, islice
from euler.lib import util
from euler.lib.primes import is_prime, primes


def rtrunc(n):
    digits = util.digits(n)
    while digits:
        yield util.undigits(digits)
        digits = digits[1:]


def ltrunc(n):
    digits = util.digits(n)
    while digits:
        yield util.undigits(digits)
        digits = digits[:-1]


def is_truncatable(n):
    return all(map(
        is_prime,
        chain(rtrunc(n), ltrunc(n))))


def truncatables():
    acceptable_primes = dropwhile(
        lambda x: x <= 7,
        primes())

    return islice(
        filter(is_truncatable,
               acceptable_primes),
        11)


def main():
    return sum(truncatables())
