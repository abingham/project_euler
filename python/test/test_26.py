from itertools import islice
from euler.exercises.ex0026 import main, unit_fraction


def test_unit_fraction():
    assert unit_fraction(2) == ([0, 5], 0)
    assert unit_fraction(3) == ([0, 3], 1)
    assert unit_fraction(4) == ([0, 2, 5], 0)
    assert unit_fraction(5) == ([0, 2], 0)
    assert unit_fraction(6) == ([0, 1, 6], 1)
    assert unit_fraction(7) == ([0, 1, 4, 2, 8, 5, 7], 6)
    assert unit_fraction(8) == ([0, 1, 2, 5], 0)
    assert unit_fraction(9) == ([0, 1], 1)
    assert unit_fraction(10) == ([0, 1], 0)


def test_main():
    assert main() == 983
