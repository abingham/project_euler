from collections import Counter

import euler.util
from hypothesis import assume, given
import hypothesis.strategies as ST


def test_is_even_is_true_for_2():
    assert euler.util.is_even(2)


def test_is_even_is_true_for_0():
    assert euler.util.is_even(0)


def test_is_even_is_false_for_1():
    assert not euler.util.is_even(1)


def test_prime_factors():
    actual = euler.util.prime_factors(13195)
    expected = Counter((1, 5, 7, 13, 29))
    assert actual == expected


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
        assert sorted(euler.util.factors(n)) == sorted(fs)


@given(ST.text())
def test_palindrome_is_false_for_non_palindromes(s):
    assume(s != ''.join(reversed(s)))
    assert not euler.util.palindrome(s)


@given(ST.text())
def test_palindrome_is_true_for_non_palindromes(s):
    s = s + ''.join(reversed(s))
    assert euler.util.palindrome(s)
