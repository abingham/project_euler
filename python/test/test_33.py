from fractions import Fraction

from euler.exercises.ex0033 import is_curious, main, nontrivial_curious, is_trivial


def test_is_curious():
    assert is_curious(49, 98)
    assert is_curious(30, 50)


def test_nontrivial_curious():
    assert (49, 98) in tuple(nontrivial_curious())


def test_trivial():
    assert is_trivial(30, 50)


def test_main():
    assert main() == 100
