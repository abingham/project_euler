from euler.exercises.ex0025 import first_of_length, main


def test_infrastructure():
    assert first_of_length(3) == 12


def test_main():
    assert main() == 4782
