from euler.exercises.ex0030 import sum_of_values, main
import pytest


def test_infrastructure():
    assert sum_of_values(4) == 19316


@pytest.mark.slow
def test_main():
    assert main() == 443839
