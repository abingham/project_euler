import cmath
from collections import Counter
from functools import reduce
from itertools import chain, combinations, count
import math
import operator
import time
import euler.lib.primes


def is_even(x):
    """Determine if an integer is even."""
    return x % 2 == 0


def digits(num):
    '''
    returns a list of the digits in num.
    Note that this returns an empty list if num is zero
    '''
    rval = []
    while num > 0:
        (num, mod) = divmod(num, 10)
        rval.append(mod)
    rval.reverse()
    return rval


def undigits(digits):
    '''
    given a list of digits, this produces the number
    that they represent. [1,2,3] -> 123
    '''
    sum = 0
    for d in digits:
        sum *= 10
        sum += d
    return sum


def length(x):
    '''returns the length in decimal digits of a number. Note that this
    returns 1 if x is zero.
    '''
    if x == 0:
        return 1
    return int(math.log10(x)) + 1


def num_cat(x, y):
    'concatenates two numbers. x,y->xy'
    return x * pow(10, length(y)) + y


hex2bin = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'a': '1010',
    'b': '1011',
    'c': '1100',
    'd': '1101',
    'e': '1110',
    'f': '1111'
}


def bin(n):
    '''
    converts a number to its binary representation
    '''
    rval = [hex2bin[h] for h in '%x' % n]
    rval = ''.join(rval).lstrip('0')
    return rval or '0'


def least_common_multiple(divisors):
    """Find small integer that is a multiple of each of a set of multiples.

    Args:
        divisors: iterable of integers to find the LCM of.

    Returns: The smallest number that is a multiple of each elements of
        `divisors`.
    """
    factors = reduce(operator.or_,
                     map(euler.lib.primes.prime_factors, divisors),
                     Counter())
    return reduce(operator.mul,
                  (f ** c for f, c in factors.items()),
                  1)


def factors(n):
    """Get all factors of a number.

    This returns a `set` of all integers that divide evenly into `n`.

    Args:
        n: The number to find the factors of.

    Returns: The set of integers that evenly divide into `n`.
    """
    pfs = tuple(euler.lib.primes.prime_factors(n).elements())
    return set(reduce(operator.mul, selection, 1)
               for selection
               in selections(pfs))


def selections(seq):
    """All combinations of all sizes of a sequence.

    Args:
        iterable: Any sequence object

    Returns: An iterable of combinations of elements from `iterable`. The
        combinations will be of size `[1-len(seq)]`. The order of the
        combinations is not guaranteed.
    """
    return chain(*(combinations(seq, n)
                   for n
                   in range(1, len(seq) + 1)))


def palindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[-1 * (i + 1)]:
            return False
    return True


def time_function(f):
    '''
    Times a call to f(), returning the tuple
    (<f's return value>, <elapsed time>)
    '''
    t1 = time.clock()
    x = f()
    return (x, time.clock() - t1)


def fact(n):
    return reduce(operator.mul, range(2, n+1), 1)


_all_digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def pandigital(l):
    d = reduce(lambda x, y: x + digits(y), l, [])
    d.sort()
    return d == _all_digits


def word_value(sz):
    '''
    sums up the ordinal values of the letters in a word
    '''
    ord_base = ord('A') - 1
    return sum([ord(l) - ord_base for l in sz.upper()])


def triangle(i):
    return i * (i + 1) // 2


def triangles():
    for i in count(1):
        yield triangle(i)


def square(i):
    return pow(i, 2)


def squares():
    for i in count(1):
        yield square(i)


def is_square(x):
    x = math.sqrt(x)
    return (x == int(x))


def pentagonals():
    for i in count(1):
        yield pentagonal(i)


def pentagonal(i):
    return i * (3 * i - 1) / 2


def hexagonal(i):
    return i * (2 * i - 1)


def hexagonals():
    for i in count(1):
        yield hexagonal(i)


def heptagonal(i):
    return i * (5 * i - 3) / 2


def heptagonals():
    for i in count(1):
        yield heptagonal(i)


def octagonal(i):
    return i * (3 * i - 2)


def octagonals():
    for i in count(1):
        yield octagonal(i)


def quadratic_roots(a, b, c):
    '''
    returns (root1, root2)

    '''
    c1 = -1.0 * b
    c2 = cmath.sqrt(math.pow(b, 2) - 4 * a * c)
    c3 = 2 * a

    return (c1 + c2) / c3, (c1 - c2) / c3


def sqrt_continued_fraction(a):
    '''
    Calculates the periodic continued fraction for the square root of a
    '''

    def new_b(x, b, c):
        return -1 * (b - x * c)

    def new_c(x, a, b, c):
        return (a - int(pow(b - x * c, 2))) / c

    x = int(math.sqrt(a))
    b = new_b(x, 0, 1)
    c = new_c(x, a, 0, 1)

    rval = [x]

    while True:
        x = int((math.sqrt(a) + b) / c)
        rval.append(x)
        # print a, b,c,x
        if c == 1:
            return rval

        b, c = (new_b(x, b, c), new_c(x, a, b, c))


def convergent(cf):
    '''
    calculates the convergent represented by a continued fraction
    '''

    c = 1
    b = cf[-1]
    for a in reversed(cf[:-1]):
        b, c = (c, b)
        b = a * c + b
    return (b, c)


def eulers_totient(x, prime_values=None):
    rslt = 1

    pfs = euler.lib.primes.prime_factors(x, prime_values)
    for prime, power in pfs:
        a = prime - 1
        b = prime ** (power - 1)

        rslt *= a * b

    return rslt


def fraction_compare(a, b):
    '''compare two fraction in tuple form (numerator,denominator)

    :return: 0 if they're equal, -1 if a < b, 1 if a > b
    '''

    x = a[0] * b[1] - a[1] * b[0]
    if x < 0:
        return -1
    elif x > 0:
        return 1
    else:
        return 0


def trace(meth):
    '''Simple function tracing decorator'''
    def new_meth(*args):
        rval = meth(*args)
        # print (meth.__name__,args,'->',rval)
        return rval
    return new_meth
