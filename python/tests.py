from itertools import islice

import euler_01
import euler_02
import euler_util
import sequences


class Test01:
    def test_internal(self):
        assert list(euler_01.lt(10, euler_01.multiples(3, 5))) == [3, 5, 6, 9]
        assert sum(euler_01.lt(10, euler_01.multiples(3, 5))) == 23

    def test_answer(self):
        assert euler_01.main() == 233168


class Test02:
    def test_answer(self):
        assert euler_02.main() == 4613732


class TestSequences:
    def test_fibonacci(self):
        assert list(islice(sequences.fibonacci(), 10)) == [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


class TestUtils:
    def test_is_even_is_true_for_2(self):
        assert euler_util.is_even(2)

    def test_is_even_is_true_for_0(self):
        assert euler_util.is_even(0)

    def test_is_even_is_false_for_1(self):
        assert not euler_util.is_even(1)
