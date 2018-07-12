from itertools import islice

from euler.exercises.ex0009 import main, pythagorean_triplets
import pytest


def test_infrastructure():
    assert (3, 4, 5) in set(islice(pythagorean_triplets(), 100))


@pytest.mark.slow
def test_main():
    assert main() == 31875000
