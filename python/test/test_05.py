from itertools import product

from euler.euler_05 import main, min_divided_by, minimize_divisors
from hypothesis import given
import hypothesis.strategies as ST


@given(ST.lists(ST.integers(min_value=1)))
def test_minimize_divisors(divisors):
    minimized = list(minimize_divisors(divisors))
    assert not any(x % y == 0
                   for x, y in product(minimized, minimized)
                   if x != y)


def test_infrastructure():
    assert min_divided_by(range(1, 11)) == 2520


def test_answer():
    assert main() == 232792560
