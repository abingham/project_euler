from itertools import takewhile
import bisect, cmath, math, operator, time

from .primes import Primes


def is_even(x):
    """Determine if an integer is even."""
    return x % 2 == 0


def bsearch(l,x,comp=None):
    '''
    Searches a sorted list for x. If it's found, return
    the index, otherwise return -1
    '''

    idx = bisect.bisect_left(l,x)
    try:
        if l[idx] == x:
            return idx
        else:
            return -1
    except IndexError:
        return -1

class GenFinder:
    def __init__(self, gen):
        self.gen = gen
        self.data = [self.gen.next()]

    def __getitem__(self, i):
        while len(self.data) <= i:
            self.data.append(self.gen.next())
        return self.data[i]

    '''
    def __setitem__(self, i, x):
        while len(self.data) <= i:
            self.data.append(self.gen.next())
        self.data[i] = x
    '''

    def __len__(self):
        return len(self.data)

    def contains(self, x):
        return self.find(x) != -1

    def find(self, x):
        if self.data[-1] < x:
            return self.find_new(x)
        else:
            return bsearch(self.data, x)

    def find_new(self, x):
        while self.data[-1] < x:
            self.data.append(self.gen.next())
        if self.data[-1] == x:
            return len(self.data) - 1
        else:
            return -1

def numbers(start=0, stride=1, max=None):
    i = start
    while max == None or i < max:
        yield i
        i += stride

def digits(num):
    '''
    returns a list of the digits in num.
    Note that this returns an empty list if num is zero
    '''
    rval = []
    while num > 0:
        (num,mod) = divmod(num, 10)
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
    '''
    returns the length in decimal digits of a number. Note that this returns 1 if
    x is zero.
    '''
    if x == 0:
        return 1
    return int(math.log10(x)) + 1

def num_cat(x,y):
    'concatenates two numbers. x,y->xy'
    return x * pow(10, length(y)) + y

hex2bin = {
    '0' : '0000',
    '1' : '0001',
    '2' : '0010',
    '3' : '0011',
    '4' : '0100',
    '5' : '0101',
    '6' : '0110',
    '7' : '0111',
    '8' : '1000',
    '9' : '1001',
    'a' : '1010',
    'b' : '1011',
    'c' : '1100',
    'd' : '1101',
    'e' : '1110',
    'f' : '1111'
}

def bin(n):
    '''
    converts a number to its binary representation
    '''
    rval = [hex2bin[h] for h in '%x' % n]
    rval = ''.join(rval).lstrip('0')
    return rval or '0'

def prime_factors(val, generator_class=Primes):
    '''
    Generates the prime factorization of val. Uses the values
    in primes as the prime numbers (so make sure it's correct!)
    Generates a list of tuples:

       [(prime, power), ...]
    '''

    max_prime = int(math.ceil(math.sqrt(val)))

    count = 0
    for prime in takewhile(lambda p: p <= max_prime, generator_class()):
        (d, m) = divmod(val, prime)
        while m == 0:
            count += 1
            val = d
            (d, m) = divmod(val, prime)
        if count != 0:
            yield (prime, count)
        if val < 2:
            break
        count = 0

    if val != 1:
        # val must be a prime itself
        yield (val, 1)

def _proper_divisors(factors):
    if len(factors) == 0:
        return [1]
    rval = []
    factor = factors[0]
    for i in xrange(0, factor[1] + 1):
        rval += [factor[0]**i * v for v in _proper_divisors(factors[1:])]
    return rval

def proper_divisors(n):
    '''
    Returns a list (not guaranteed to be sorted) of proper divisors of n
    '''
    factors = [f for f in prime_factors(n)]
    return _proper_divisors(factors)[:-1]

def permutations(tokens, size=None):
    '''
    Generates permutations of a list of tokens. This will generate all
    permutations with length up to 'size'. If size is unspecified,
    this will generate all permutations. Order is important, so selections
    can be repeated in different orders
    '''
    if size is None:
        size = len(tokens)

    if size > 0:
        for i in xrange(len(tokens)):
            tokens[0],tokens[i] = tokens[i],tokens[0]
            yield [tokens[0]]
            for rest in permutations(tokens[1:], size - 1):
                yield [tokens[0]] + rest

def opermutations(tokens):
    if len(tokens) == 0:
        yield []
    else:
        for i in xrange(len(tokens)):
            yield [tokens[i]]
            for p in opermutations(tokens[i+1:]):
                yield [tokens[i]] + p

def combos(toks):
    '''
    generates all possible orderings of 'toks'
    NOTE: You should be using itertools if possible
    '''
    if len(toks) == 1:
        yield toks
    else:
        for i in xrange(len(toks)):
            temp = operator.getitem(toks, 0)
            operator.setitem(toks, 0, operator.getitem(toks, i))
            operator.setitem(toks, i, temp)
            for rest in combos(toks[1:]):
                yield [operator.getitem(toks, 0)] + rest
            temp = operator.getitem(toks, 0)
            operator.setitem(toks, 0, operator.getitem(toks, i))
            operator.setitem(toks, i, temp)

def combinations(toks, size):
    '''
    yields all combinations of toks of a given size...order is unimportant.
    '''

    if size == 0:
        yield []
    else:
        for i in xrange(len(toks) - size + 1):
            for c in combinations(toks[i + 1:], size - 1):
                yield [toks[i]] + c

def selections(toks):
    '''
    yields all possible selections of elements from 'toks', including the
    empty set. Order is not important, so, e.g., [1,2,3] and [3,2,1] will not both
    be yielded.
    '''
    for i in xrange(len(toks) + 1):
        for c in combinations(toks, i):
            yield c


def palindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[-1 * (i + 1)]:
            return False
    return True


def fib():
    '''
    Generates fibonacci numbers. [1,1,2,3,...]
    Yields valus in the form (<index>, <value>). So the
    first yield is (1,1), second is (2,1), then (3,2), (4,3),
    and so on...
    '''
    prev = 1
    yield (1,prev)
    curr = 1
    yield (2,curr)

    idx = 3
    while True:
        rval = prev + curr
        yield (idx, rval)
        idx += 1
        prev = curr
        curr = rval

def time_function(f):
    '''
    Times a call to f(), returning the tuple
    (<f's return value>, <elapsed time>)
    '''
    t1 = time.clock()
    x = f()
    return (x, time.clock() - t1)

def fact(n):
    return reduce(operator.mul, xrange(2,n+1), 1)

_all_digits = [1,2,3,4,5,6,7,8,9]

def pandigital(l):
    d = reduce(lambda x,y: x + digits(y), l, [])
    d.sort()
    return d == _all_digits

def word_value(sz):
    '''
    sums up the ordinal values of the letters in a word
    '''
    ord_base = ord('A') - 1
    return sum([ord(l) - ord_base for l in sz.upper()])

def triangle(i):
    return i * (i + 1) / 2

def triangles():
    for i in numbers(1):
        yield triangle(i)

def square(i):
    return pow(i,2)

def squares():
    for i in numbers(1):
        yield square(i)

def is_square(x):
    x = math.sqrt(x)
    return (x == int(x))

def pentagonals():
    for i in numbers(1):
        yield pentagonal(i)

def pentagonal(i):
    return i * (3 * i - 1) / 2

def hexagonal(i):
    return i * (2 * i - 1)

def hexagonals():
    for i in numbers(1):
        yield hexagonal(i)

def heptagonal(i):
    return i * (5 * i - 3) / 2

def heptagonals():
    for i in numbers(1):
        yield heptagonal(i)

def octagonal(i):
    return i * (3 * i - 2)

def octagonals():
    for i in numbers(1):
        yield octagonal(i)

def accumulate(l, f, prev):
    results = []
    for i in l:
        prev = f(prev, i)
        results.append(prev)
    return results

def quadratic_roots(a,b,c):
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

    new_b = lambda x,b,c : -1 * (b - x * c)
    new_c = lambda x,a,b,c: (a - int(pow(b - x * c, 2))) / c

    x = int(math.sqrt(a))
    b = new_b(x,0,1)
    c = new_c(x,a,0,1)

    rval = [x]

    while True:
        x = int((math.sqrt(a) + b) / c)
        rval.append(x)
        # print a, b,c,x
        if c == 1:
            return rval

        b,c = (new_b(x,b,c), new_c(x,a,b,c))

def convergent(cf):
    '''
    calculates the convergent represented by a continued fraction
    '''

    c = 1
    b = cf[-1]
    for a in reversed(cf[:-1]):
        b,c = (c,b)
        b = a * c + b
    return (b,c)

def eulers_totient(x, prime_values = None):
    rslt = 1

    pfs = prime_factors(x, prime_values)
    for prime,power in pfs:
        a = prime - 1
        b = prime ** (power - 1)

        rslt *= a * b

    return rslt

def fraction_compare(a,b):
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

def main():
    pass # print ([p for p in opermutations([0,1,2,3])])

if __name__ == '__main__':
    main()
