from itertools import count, takewhile
import math
import pkg_resources
from zipfile import ZipFile
from collections import Counter


class PrimesCalculator:
    def __init__(self):
        self._priors = [2]

    def _is_prime(self, x):
        """
        helper function for gen_primes. This determines if x is a prime number,
        given the list 'priors' which is all primes less than x.
        """
        s = math.ceil(math.sqrt(x))
        priors = takewhile(lambda i: i <= s, self._priors)
        if any(x % prior == 0 for prior in priors):
            return False
        return True

    def __iter__(self):
        '''
        an unbounded generator of primes starting at 2
        '''
        yield 2
        for n in count(start=3, step=2):
            if self._is_prime(n):
                yield n
                self._priors.append(n)


class PrimesReader:
    def __iter__(self):
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


Primes = PrimesReader


def prime_factors(val, generator_class=Primes, include_one=True):
    '''Generates the prime factorization of val. Uses the values in primes as the
    prime numbers (so make sure it's correct!)

    Args:
        val: The value to factor
        generator_class: The unary callable that produces a sequence of primes
        include_one: Whether 1 should be included in the output

    Returns: A `collectons.Counter` of primes mapped to their counts in the
        factorization.
    '''

    max_prime = int(math.ceil(math.sqrt(val)))
    factors = Counter()
    if include_one:
        factors[1] = 1

    for prime in takewhile(lambda p: p <= max_prime, generator_class()):
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