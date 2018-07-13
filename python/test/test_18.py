from euler.exercises.ex0018 import main, max_path


def test_infrastructure():
    lattice = (
        (3,),
        (7, 4),
        (2, 4, 6),
        (8, 5, 9, 3),
    )

    assert max_path(lattice) == 23


def test_main():
    assert main() == 1074
