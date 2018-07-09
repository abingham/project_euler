from itertools import count, takewhile
import math


class Primes:
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


# def read_primes_(filenames):
#     '''
#     Takes a list of zip filenames, reading them each in order
#     as lists of prime numbers. This is a generator where each
#     yield produces the next prime read in.
#     '''
#     for filename in filenames:
#         zfile = zipfile.ZipFile(filename, 'r')
#         for name in zfile.namelist():
#             file = zfile.open(name)
#             for line in file:
#                 for prime in line.split():
#                     try:
#                         yield int(prime)
#                     except ValueError:
#                         continue
#         zfile.close()

# def read_primes(filenames=[]):
#     '''generate a sequence of primes read from files

#     :param filenames: a list of filenames to read primes from. If
#                       empty, a list of all files in the prime_data
#                       directory is used (in proper order)
#     :return: a generator of primes
#     '''
#     if len(filenames) == 0:
#         filenames = [os.path.join('prime_data', 'primes%d.zip' % i) for i in xrange(1, 51)]
#     return read_primes_(filenames)

# def primes(up_to):
#     '''
#     generates a list of primes in the range [2,up_to]
#     '''
#     if up_to == 0:
#         return

#     candidates = [True for i in xrange(up_to + 1)]
#     candidates[0] = False
#     candidates[1] = False

#     i = 0
#     l = len(candidates)
#     while i < l:
#         if not candidates[i]:
#             i += 1
#             continue

#         yield i

#         j = i
#         while j < l:
#             candidates[j] = False
#             j += i
#         i += 1
