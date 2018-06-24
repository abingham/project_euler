"""2520 is the smallest number that can be divided by each of the numbers from
1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?

"""

from itertools import count


def min_divided_by(divisors):
    divisors = sorted(divisors, reverse=True)
    return next(
        val
        for val in count(1)
        if all(val % d == 0 for d in divisors))

def main():
    return min_divided_by(range(1, 21))
