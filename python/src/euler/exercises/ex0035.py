"""The number, 197, is called a circular prime because all rotations of the
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71,
73, 79, and 97.

How many circular primes are there below one million?
"""

from more_itertools import ilen

from euler.lib.primes import is_prime
from euler.lib import util


def rotations(n):
    digits = util.digits(n)
    for i in range(len(digits)):
        yield util.undigits(digits)
        digits = digits[1:] + digits[0:1]


def is_circular(n):
    return all(map(is_prime, rotations(n)))


def main():
    return ilen(n
                for n
                in range(2, 1000001)
                if is_circular(n))


