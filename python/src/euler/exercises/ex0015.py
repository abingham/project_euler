"""Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

from more_itertools import nth

from euler.lib.util import is_even
import euler.lib.sequences


def lattice_paths(n):
    level = nth(euler.lib.sequences.pascals_triangle(), 2 * n)
    assert not is_even(len(level))
    return level[len(level) // 2]


def main():
    return lattice_paths(20)
