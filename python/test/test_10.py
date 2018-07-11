from euler.euler_10 import main, sum_of_primes_below


def test_infrastructure():
    assert sum_of_primes_below(10) == 17


def test_main():
    assert main() == 142913828922
