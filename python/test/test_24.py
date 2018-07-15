from euler.exercises.ex0024 import main, sorted_permutations
import pytest


@pytest.mark.slow
def test_main():
    assert main() == '5468731092'
