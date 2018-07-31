from euler.exercises.ex0037 import is_truncatable, ltrunc, main, rtrunc


def test_rtrunc():
    assert list(rtrunc(3797)) == [3797, 797, 97, 7]


def test_ltrunc():
    assert list(ltrunc(3797)) == [3797, 379, 37, 3]


def test_main():
    assert main() == 748317
