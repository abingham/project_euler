"""If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

from itertools import count, takewhile


def multiples(*factors):
    """Iterable of integers which are multiples of elements of `factors`.
    """
    for i in count(1):
        if any(i % f == 0 for f in factors):
            yield i


def lt(limit, iterable):
    """Iterable of elements of `iterable` which are less than `limit`.
    """
    return takewhile(lambda i: i < limit, iterable)

assert list(lt(10, multiples(3, 5))) == [3, 5, 6, 9]
assert sum(lt(10, multiples(3, 5))) == 23

def main():
    return sum(lt(1000, multiples(3, 5)))
