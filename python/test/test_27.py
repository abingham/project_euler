from euler.exercises.ex0027 import main, num_primes
import pytest


def test_infrastructure():
    assert num_primes(1, 41) == 40
    assert num_primes(-79, 1601) == 80


@pytest.mark.slow
def test_main():
    assert main() == -59231
