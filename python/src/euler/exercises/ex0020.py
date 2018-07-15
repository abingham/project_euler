"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

from math import factorial

from euler.lib import util


def sum_fact_digits(n):
    f = factorial(n)
    digits = util.digits(f)
    return sum(digits)


def main():
    return sum_fact_digits(100)
