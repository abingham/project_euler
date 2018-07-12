from euler.exercises.ex0015 import lattice_paths, main


def test_infrastructure():
    assert lattice_paths(1) == 2
    assert lattice_paths(2) == 6


def test_main():
    assert main() == 137846528820
