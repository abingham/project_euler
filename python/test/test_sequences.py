from itertools import islice
from euler.lib.sequences import collatz, fibonacci


def test_fibonacci():
    assert list(islice(fibonacci(), 10)) == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


def test_collatz():
    actual = list(collatz(13))
    expected = [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    assert len(expected) == 10
    assert actual == expected
