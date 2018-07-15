"""A unit fraction contains 1 in the numerator. The decimal representation of
the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle
in its decimal fraction part.
"""

from itertools import count, islice

def unit_fraction(denominator):
    """Get the digits of a unit fraction.

    A unit fraction is a fraction with a 1 in the numerator. So
    the unit fraction for 7 is 1/7. This function produces:

        >>> list(islice(unit_fraction(7), 10))
        [0, 1, 4, 2, 8, 5, 7, 1, 4, 2]

    Args:
        denominator: The denominator of the unit fraction.

    Returns: A tuple of (digits, cycle-length). If cycle-length is not zero,
         then the last `cycle-length` digits in `digits` cycle forever.
    """
    history = {}
    result = []
    numerator = 1
    for distance in count():
        if numerator < denominator:
            numerator *= 10
            result.append(0)
        else:
            d, m = divmod(numerator, denominator)
            try:
                return result, distance - history[(d, m)]
            except KeyError:
                pass

            history[(d, m)] = distance

            result.append(d)
            if m == 0:
                return result, 0
            numerator = m * 10


def main():
    return max(range(1, 1000),
               key=lambda x: unit_fraction(x)[1])
