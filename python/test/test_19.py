from euler.exercises.ex0019 import is_leap_year, main


def test_is_leap_year():
    assert is_leap_year(2000)
    assert not is_leap_year(1900)
    assert is_leap_year(1952)


def test_main():
    assert main() == 171
