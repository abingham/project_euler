from euler.exercises.ex0001 import lt, main, multiples


def test_internal():
    assert list(lt(10, multiples(3, 5))) == [3, 5, 6, 9]
    assert sum(lt(10, multiples(3, 5))) == 23


def test_answer():
    assert main() == 233168
