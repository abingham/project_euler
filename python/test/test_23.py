from euler.exercises.ex0023 import abundants, is_abundant, main


def test_is_abundant():
    assert is_abundant(12)


def test_12_is_abundant():
    assert next(abundants()) == 12


def test_main():
    assert main() == 4179871
