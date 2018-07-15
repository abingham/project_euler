from euler.exercises.ex0020 import main, sum_fact_digits


def test_infrastructure():
    assert sum_fact_digits(10) == 27


def test_main():
    assert main() == 648
