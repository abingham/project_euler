import bisect, math
import euler_util

def rtrunc(x):
    return x / 10

def ltrunc(x):
    if x == 0:
        return 0
    p = 10 ** int(math.log10(x))
    return x - (x / p) * p

def curious(x, primes):
    # First, check right truncation
    val = x
    for i in range(euler_util.length(x) - 1):
        val = rtrunc(val)
        if euler_util.bsearch(primes, val) == -1:
            return False

    # next, check left truncation
    val = x
    for i in range(euler_util.length(x) - 1):
        val = ltrunc(val)
        if euler_util.bsearch(primes, val) == -1:
            return False

    return True

def run():
    pgen = euler_util.gen_primes()

    # initialize primes list with single-digit primes...we don't consider those for rotation
    primes = [pgen.next(), pgen.next(), pgen.next(), pgen.next()]
    results = []

    while len(results) < 11:
        prime = pgen.next()
        primes.append(prime)
        if curious(prime, primes):
            # print prime
            results.append(prime)

    # print sum(results)

def test():
    # 3797
    primes = [379,37,3,797,97,7]
    primes.sort()
    # print curious(3797, primes)

run()
