from itertools import islice
from euler.sequences import fibonacci


def test_fibonacci():
    assert list(islice(fibonacci(), 10)) == [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
