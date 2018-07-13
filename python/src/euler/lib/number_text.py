from more_itertools import grouper

from euler.lib import util

ONES = (
    '',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine'
)

TEENS = (
    'ten',
    'eleven',
    'twelve',
    'thirteen',
    'fourteen',
    'fifteen',
    'sixteen',
    'seventeen',
    'eighteen',
    'nineteen'
)

TENS = (
    '',
    '',
    'twenty',
    'thirty',
    'forty',
    'fifty',
    'sixty',
    'seventy',
    'eighty',
    'ninety'
)

MAGNITUDES = (
    '',
    'thousand',
    'million',
    'billion',
    'trillion',
)


def _group_by_thousands(x):
    """Sequence of (magnitude, chunk) tuples.

    `magnitude` is an integer representing which "group of thousands" the chunk
    represents. So 0 means "0 through 999", 1 means "1000 to 9999", etc.

    `chunk` is a tuple of three integers representing the digits of the current
    chunk.

    The iteration will be in order from greatest magnitude to smallest.
    """
    digits = util.digits(x)

    # Groups by thousands
    chunks = list(enumerate(grouper(3, reversed(digits))))
    chunks.reverse()

    for magnitude, chunk in chunks:
        chunk = tuple(0 if d is None else d for d in reversed(chunk))
        yield magnitude, chunk


def _chunk_tens(chunk):
    """Get the 'tens' portion of a chunk, i.e. the text for the portion less than
    100.
    """
    if chunk[1] == 1:
        return TEENS[chunk[2]]

    tens = TENS[chunk[1]]
    ones = ONES[chunk[2]]
    return '{tens}{sep}{ones}'.format(
        tens=tens,
        sep='-' if tens and ones else '',
        ones=ones)


def _chunk_hundreds(chunk):
    """Get the 'hundreds' portion of a chunk, i.e. the text for the portion greater
    than 99.
    """
    if chunk[0] == 0:
        return ''

    return '{} hundred'.format(ONES[chunk[0]])


def _chunk_text(chunk):
    """Get the complete text for a chunk, without magnitude.
    """
    assert 0 < len(chunk) < 4

    hundreds = _chunk_hundreds(chunk)
    tens = _chunk_tens(chunk)
    return '{hundreds}{hsep}{tens}'.format(
        hundreds=hundreds,
        hsep=' and ' if hundreds and tens else '',
        tens=_chunk_tens(chunk)
    )


def _add_magnitude(chunk, mag):
    return '{} {}'.format(chunk, MAGNITUDES[mag]).strip()


def number_text(x):
    """Convert a non-negative integer into English text.

    Args:
        x: The number to convert.

    Returns: A string of the English text for the number.
    """
    if x == 0:
        return 'zero'

    chunks = (_add_magnitude(_chunk_text(chunk), magnitude)
              for magnitude, chunk in _group_by_thousands(x))
    return ' '.join(filter(None, chunks))
