from euler.exercises.ex0032 import main, pandigitals


def test_infrastructure():
    assert {39, 186, 7254} in [set(pd) for pd in pandigitals()]


def test_main():
    assert main() == 45228
