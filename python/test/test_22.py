from euler.exercises.ex0022 import load_names, main, score


def test_score():
    assert score('COLIN', 938) == 49714


def test_loaded_names():
    assert load_names()[937] == 'COLIN'


def test_main():
    assert main() == 871198282
