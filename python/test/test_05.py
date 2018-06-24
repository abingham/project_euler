from euler.euler_05 import main, min_divided_by


def test_infrastructure():
    assert min_divided_by(range(1, 11)) == 2520


def test_answer():
    assert main() == 232792560
