from euler.exercises.ex0006 import main, square_of_sum, sum_of_squares


def test_infrastructure():
    assert sum_of_squares(10) == 385
    assert square_of_sum(10) == 3025
    assert square_of_sum(10) - sum_of_squares(10) == 2640


def test_main():
    assert main() == 25164150
