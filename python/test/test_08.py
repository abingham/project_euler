from euler.euler_08 import NUMBER, main, max_product


def test_infrastructure():
    assert max_product(NUMBER, 4) == 5832


def test_main():
    assert main() == 23514624000
