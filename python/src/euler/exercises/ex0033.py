"""The fraction 49/98 is a curious fraction, as an inexperienced mathematician
in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is
correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than
one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms,
find the value of the denominator.
"""

from fractions import Fraction
from functools import reduce
from itertools import count, islice
from math import gcd
from euler.lib.util import digits, undigits


def reduced(num, den):
    ndigits = list(digits(num))
    ddigits = list(digits(den))

    for dig in tuple(ndigits):
        if dig in ddigits:
            ndigits.remove(dig)
            ddigits.remove(dig)

    return undigits(ndigits), undigits(ddigits)


def is_curious(num, den):
    try:
        nnum, nden = reduced(num, den)
        return (num != nnum and
                den != nden and
                Fraction(nnum, nden) == Fraction(num, den))
    except (ValueError, ZeroDivisionError):
        return False


def is_trivial(num, den):
    """A fraction is trivial if:
    a) Both he numerator and denominator end in the same number of zeros, and
    b) They share no other common digits beyond the trailing zeros.
    """
    return gcd(num, den) % 10 == 0


def curious():
    for den in count(1):
        for num in range(1, den):
            if is_curious(num, den) and not is_trivial(num, den):
                yield num, den


def nontrivial_curious():
    return islice(
        ((n, d) for n, d in curious() if not is_trivial(n, d)),
        4)


def main():
    return reduce(
        lambda acc, n: acc * Fraction(n[0], n[1]),
        nontrivial_curious(),
        Fraction(1, 1)).denominator
