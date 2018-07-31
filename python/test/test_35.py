from euler.exercises.ex0035 import is_circular, main, rotations
import pytest

def test_rotations():
    assert list(rotations(197)) == [197, 971, 719]



def test_is_circular():
    for c in [2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79,  97]:
        assert is_circular(c)


@pytest.mark.slow
def test_main():
    assert main() == 55
