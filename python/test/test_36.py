from euler.exercises.ex0036 import main, multi_palindrome


def test_multi_palindrome():
    assert multi_palindrome(585)


def test_main():
    assert main() == 872187
