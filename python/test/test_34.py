from euler.exercises.ex0034 import curious, is_curious, main


def test_is_curious():
    assert is_curious(145)
    assert not is_curious(1)
    assert not is_curious(2)


def test_curious():
    assert 145 in tuple(curious())


def test_main():
    assert main() == 40730
