import euler.util


def test_is_even_is_true_for_2():
    assert euler.util.is_even(2)


def test_is_even_is_true_for_0():
    assert euler.util.is_even(0)


def test_is_even_is_false_for_1():
    assert not euler.util.is_even(1)
