from euler.exercises.ex0021 import amicable, d, main
import pytest


def test_d():
    assert d(220) == 284
    assert d(284) == 220


def test_amicable():
    assert amicable(220)
    assert amicable(284)


@pytest.mark.slow
def test_main():
    assert main() == 31626
