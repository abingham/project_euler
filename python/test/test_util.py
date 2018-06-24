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
    factors = euler.util.prime_factors(13195)
    actual = sorted(f[0] for f in factors)
    expected = [5, 7, 13, 29]
    assert actual == expected


@given(ST.text())
def test_palindrome_is_false_for_non_palindromes(s):
    assume(s != ''.join(reversed(s)))
    assert not euler.util.palindrome(s)


@given(ST.text())
def test_palindrome_is_true_for_non_palindromes(s):
    s = s + ''.join(reversed(s))
    assert euler.util.palindrome(s)
