from euler.lib.util import is_even

def fibonacci():
    """Iterable of the Fibonacci sequence."""
    curr = 1
    next = 2
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
