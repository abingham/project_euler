from euler.exercises.ex0014 import main
import pytest


@pytest.mark.slow
def test_main():
    assert main() == 837799
