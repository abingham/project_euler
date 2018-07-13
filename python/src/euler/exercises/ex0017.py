from euler.lib.number_text import number_text


REMOVE_UNCOUNTED_CHARS = str.maketrans({' ': None, '-': None})


def number_size(x):
    """The number of characters in the text version of a number.

    This count excludes spaces and hyphens.
    """
    s = number_text(x).translate(REMOVE_UNCOUNTED_CHARS)
    return len(s)


def num_letters(values):
    """Sum of number-sizes for all values in an iterable.
    """
    return sum(number_size(value) for value in values)


def main():
    return num_letters(range(1, 1001))
