from itertools import count, islice, takewhile
import math
import pkg_resources
from zipfile import ZipFile
from collections import Counter

from euler.lib.bisect import contains


def primes():
    # TODO: This should be expanded to process *all* zipfiles found in the
    # "primes" directory

    filename = pkg_resources.resource_filename(
        'euler', 'data/primes/primes1.zip')

    with ZipFile(filename, mode='r') as archive:
        for filename in sorted(archive.namelist()):
            with archive.open(filename) as handle:
                for line in handle:
                    try:
                        yield from [int(tok) for tok in line.split()]
                    except ValueError:
                        pass


class _PrimesCache:
    def __init__(self, block_size=1000):
        self._src = iter(primes())
        self._block_size = block_size
        self._cache = []

    def _extend_to_value(self, n):
        while not self._cache or self._cache[-1] < n:
            self._cache.extend(islice(self._src, self._block_size))

    def __contains__(self, n):
        self._extend_to_value(n)
        return contains(self._cache, n)


_cache = _PrimesCache()

def is_prime(n):
    return n in _cache


def prime_factors(val, include_one=True):
    '''Generates the prime factorization of val. Uses the values in primes as the
    prime numbers (so make sure it's correct!)

    Args:
        val: The value to factor
        include_one: Whether 1 should be included in the output

    Returns: A `collectons.Counter` of primes mapped to their counts in the
        factorization.
    '''

    max_prime = int(math.ceil(math.sqrt(val)))
    factors = Counter()

    if val == 0:
        return factors

    if include_one:
        factors[1] = 1

    for prime in takewhile(lambda p: p <= max_prime, primes()):
        (d, m) = divmod(val, prime)
        while m == 0:
            factors[prime] += 1
            val = d
            (d, m) = divmod(val, prime)

        if val < 2:
            break

    if val != 1:
        # val must be a prime itself
        factors[val] = 1

    return factors
