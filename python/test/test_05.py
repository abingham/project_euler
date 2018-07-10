from euler.euler_05 import least_common_multiple, main


def test_infrastructure():
    assert least_common_multiple(range(1, 11)) == 2520


def test_answer():
    assert main() == 232792560
