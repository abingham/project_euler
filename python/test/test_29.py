from euler.exercises.ex0029 import distinct_terms, main


def test_infrastructure():
    assert distinct_terms(range(2, 6), range(2, 6)) == 15


def test_main():
    assert main() == 9183
