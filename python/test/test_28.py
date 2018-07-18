from euler.exercises.ex0028 import diagonal_sum, main


def test_infrastructure():
    assert diagonal_sum(5) == 101


def test_main():
    assert main() == 669171001
