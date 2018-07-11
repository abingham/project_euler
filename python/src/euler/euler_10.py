"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from itertools import takewhile
from euler.primes import Primes


def sum_of_primes_below(n):
    return sum(takewhile(lambda x: x < n, Primes()))


def main():
    return sum_of_primes_below(2e6)
