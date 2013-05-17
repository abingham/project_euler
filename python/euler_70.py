import math

import euler_util as eu

def permutations(x,y):
    xs = [0] * 10

    while x > 0:
        x,m = divmod(x,10)
        xs[m] += 1

    while y > 0:
        y,m = divmod(y,10)
        xs[m] -= 1

    return reduce(lambda x,y: (y == 0) and x, xs, True)

def run(tgt):
    primes = list(eu.primes(int(math.ceil(math.sqrt(tgt)) * 2)))
    print 'primes generated'

    print primes[-1]

    min_ratio = None
    min_n = 0

    for i in range(len(primes) - 1, -1, -1):
        for j in range(i, -1, -1):
            pi = primes[i]
            pj = primes[j]
            n = pi * pj

            if n > tgt:
                continue
            phi = (pi - 1) * (pj - 1)
            
            if not permutations(n, phi):
                continue

            ratio = n / float(phi)
            if min_ratio is None or ratio < min_ratio:
                min_ratio = ratio
                min_n = n

    print min_n

if __name__ == '__main__':
    run(10000000)
