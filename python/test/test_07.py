from euler.exercises.ex0007 import main, nth_prime


def test_infrastructure():
    assert nth_prime(6) == 13


def test_main():
    assert main() == 104743
