"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 2^5 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

from itertools import count


def pythagorean_triplets():
    "Iterable of all Pythagorean triplets."
    return ((a, b, c)
            for c in count(3)
            for b in range(2, c)
            for a in range(1, b)
            if a**2 + b ** 2 == c ** 2)


def main():
    return next(a * b * c
                for a, b, c
                in pythagorean_triplets()
                if a + b + c == 1000)
