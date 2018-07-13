from euler.exercises.ex0017 import main, number_size, num_letters


def test_infrastructure():
    assert num_letters(range(1, 6)) == 19
    assert number_size(342) == 23
    assert number_size(115) == 20


def test_main():
    assert main() == 21124
