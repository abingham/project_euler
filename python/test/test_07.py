from euler.euler_07 import main, nth_prime


def test_infrastructure():
    assert nth_prime(6) == 13


def test_main():
    assert main() == 104743
