from euler.exercises.ex0012 import first_triangle_with_n_divisors, main
import pytest


def test_infrastructure():
    assert first_triangle_with_n_divisors(5) == 28


@pytest.mark.slow
def test_main():
    assert main() == 76576500
