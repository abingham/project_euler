from euler.lib.util import is_even
from itertools import chain


def pascals_triangle():
    """The levels of Pascal's triangle.

    Returns: An iterable of sequences where each sequence contains the values
        at that level.
    """
    level = (1,)
    while True:
        yield level
        top = chain(level, [0])
        bottom = chain([0], level)
        level = tuple(a + b for a, b in zip(top, bottom))


def fibonacci():
    """Iterable of the Fibonacci sequence."""
    curr = 1
    next = 1
    while True:
        yield curr
        curr, next = next, curr + next


def collatz(n):
    """Generate collatz sequence for n.

    Returns: An iterable of the Collatz sequence starting at `n` and ending at
        1 (presumably!).
    """
    while n != 1:
        yield n
        if is_even(n):
            n = n // 2
        else:
            n = 3 * n + 1

    assert n == 1
    yield n
