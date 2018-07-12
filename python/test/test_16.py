from euler.exercises.ex0016 import main, sum_of_digits


def test_infrastructure():
    assert sum_of_digits(2 ** 15) == 26


def test_main():
    assert main() == 1366
