"""We shall say that an n-digit number is pandigital if it makes use of all
the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1
through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can
be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.
"""

from math import floor, log10

from euler.lib.util import digits


PANDIGITS = set(range(1, 10))

def pandigital(digits):
    return len(digits) == len(PANDIGITS) and set(digits) == PANDIGITS


def pandigitals():
    for left in range(1, 10000):
        left_magnitude = floor(log10(left))
        right_magnitude = 3 - left_magnitude  # Do the math. I promise this is legit.
        right_start = 10 ** right_magnitude
        right_end = 10 ** (right_magnitude + 1)
        for right in range(right_start, right_end):
            product = left * right
            if pandigital(digits(left) + digits(right) + digits(product)):
                yield (left, right, product)


def main():
    return sum(set(product
                   for _, _, product
                   in pandigitals()))
