def fibonacci():
    """Iterable of the Fibonacci sequence."""
    curr = 1
    next = 2
    while True:
        yield curr
        curr, next = next, curr + next
