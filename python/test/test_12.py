from euler.euler_12 import first_triangle_with_n_divisors, main


def test_infrastructure():
    assert first_triangle_with_n_divisors(5) == 28


def test_main():
    assert main() == 76576500
