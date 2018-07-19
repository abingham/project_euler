from euler.exercises.ex0031 import main, sum_to
import pytest

@pytest.mark.slow
def test_infrastructure():
    assert (100, 50, 20, 20, 5, 2, 1, 1, 1) in set(sum_to(200))


@pytest.mark.slow
def test_main():
    assert main() == 73682
