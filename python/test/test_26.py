from itertools import islice
from euler.exercises.ex0026 import cycle_length, main, unit_fraction


def test_unit_fraction():
    assert tuple(unit_fraction(2)) == (0, 5)
    assert tuple(islice(unit_fraction(3), 2)) == (0, 3)
    assert tuple(unit_fraction(4)) == (0, 2, 5)
    assert tuple(unit_fraction(5)) == (0, 2)
    assert tuple(islice(unit_fraction(6), 3)) == (0, 1, 6)
    assert tuple(islice(unit_fraction(7), 7)) == (0, 1, 4, 2, 8, 5, 7)
    assert tuple(unit_fraction(8)) == (0, 1, 2, 5)
    assert tuple(islice(unit_fraction(9), 2)) == (0, 1)
    assert tuple(unit_fraction(10)) == (0, 1)


def test_cycle_length():
    assert cycle_length(6) == 1
    assert cycle_length(7) == 6


def test_main():
    assert main() == 81
