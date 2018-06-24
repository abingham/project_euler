"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

from itertools import takewhile

from euler.util import is_even
from sequences import fibonacci


def main():
    vals = takewhile(lambda i: i < 4000000, fibonacci())
    vals = filter(is_even, vals)
    return sum(vals)
