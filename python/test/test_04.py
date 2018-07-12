from euler.exercises.ex0004 import main, products
from euler.lib.util import palindrome


def test_infrastructure():
    p = products(10, 99)
    assert max(x for x in p if palindrome(str(x))) == 9009


def test_answer():
    assert main() == 906609
