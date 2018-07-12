"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10 001st prime number?
"""


from euler.lib.primes import Primes
from more_itertools import nth


def nth_prime(n):
    return nth(Primes(), n - 1)


def main():
    return nth_prime(10001)
