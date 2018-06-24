from itertools import count, takewhile


def multiples(*factors):
    """Iterable of integers which are multiples of elements of `factors`.
    """
    for i in count():
        if any(i % f == 0 for f in factors):
            yield i


def lt(limit, iterable):
    """Iterable of elements of `iterable` which are less than `limit`.
    """
    return takewhile(lambda i: i < limit, iterable)


assert sum(lt(10, multiples(3, 5))) == 23

print(sum(lt(1000, multiples(3, 5))))
