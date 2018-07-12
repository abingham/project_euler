from collections import Counter
from itertools import islice

import euler.lib.util
from hypothesis import assume, given
import hypothesis.strategies as ST


def test_is_even_is_true_for_2():
    assert euler.lib.util.is_even(2)


def test_is_even_is_true_for_0():
    assert euler.lib.util.is_even(0)


def test_is_even_is_false_for_1():
    assert not euler.lib.util.is_even(1)


def test_prime_factors():
    actual = euler.lib.util.prime_factors(13195)
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
        assert sorted(euler.lib.util.factors(n)) == sorted(fs)


def test_triangle_numbers():
    actual = list(islice(euler.lib.util.triangles(), 10))
    expected = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
    assert actual == expected


@given(ST.text())
def test_palindrome_is_false_for_non_palindromes(s):
    assume(s != ''.join(reversed(s)))
    assert not euler.lib.util.palindrome(s)


@given(ST.text())
def test_palindrome_is_true_for_non_palindromes(s):
    s = s + ''.join(reversed(s))
    assert euler.lib.util.palindrome(s)
