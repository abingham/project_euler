"""Starting with the number 1 and moving to the right in a clockwise direction
a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed
in the same way?
"""

def level_sum(n):
    """Sum of corners for a given level where the inner-most cell of a spiral is
    level 1.
    """
    corner_average = (4 * n ** 2 - 7 * n + 4)
    return 4 * corner_average


def diagonal_sum(side_length):
    # TODO: Can we analyze the sequence to find a non-iterative solution?
    depth = (side_length + 1) // 2
    return 1 + sum(level_sum(level) for level in range(2, depth + 1))


def main():
    return diagonal_sum(1001)
