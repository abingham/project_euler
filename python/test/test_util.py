from itertools import islice

from euler.lib import util
from hypothesis import assume, given
import hypothesis.strategies as ST


def test_is_even_is_true_for_2():
    assert util.is_even(2)


def test_is_even_is_true_for_0():
    assert util.is_even(0)


def test_is_even_is_false_for_1():
    assert not util.is_even(1)


def test_factors():
    cases = {
        1: [1],
        3: [1, 3],
        6: [1, 2, 3, 6],
        10: [1, 2, 5, 10],
        15: [1, 3, 5, 15],
        21: [1, 3, 7, 21],
        28: [1, 2, 4, 7, 14, 28],
    }

    for n, fs in cases.items():
        assert sorted(util.factors(n)) == sorted(fs)

def test_proper_divisors():
    assert util.proper_divisors(220) == {
        1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110
    }

    assert util.proper_divisors(284) == {
        1, 2, 4, 71, 142
    }


def test_triangle_numbers():
    actual = list(islice(util.triangles(), 10))
    expected = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
    assert actual == expected


@given(ST.text())
def test_palindrome_is_false_for_non_palindromes(s):
    assume(s != ''.join(reversed(s)))
    assert not util.palindrome(s)


@given(ST.text())
def test_palindrome_is_true_for_non_palindromes(s):
    s = s + ''.join(reversed(s))
    assert util.palindrome(s)
