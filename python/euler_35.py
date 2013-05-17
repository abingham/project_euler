import bisect, math
import euler_util

primes = [i for i in euler_util.primes(1000001)]

def rotate(n):
    d,m = divmod(n,10)
    return d + m * (10**int(math.log10(n)))

def is_prime(n):
    return euler_util.bsearch(primes, n) != -1

def circular(n):
    if not is_prime(n):
        return False
    for i in range(math.log10(n)):
        n = rotate(n)
        if not is_prime(n):
            return False
    return True

def run():
    results = set()
    for i in range(1000000):
        if circular(i):
            print i
            results.add(i)
        
    print len(results)

def test():
    print is_prime(5)
    print is_prime(13)
    print is_prime(34)
    print is_prime(100)

run()
