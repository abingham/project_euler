import euler_util
import math

def is_prime(x, primes):
    s = math.sqrt(x)
    for prime in primes:
        if prime > s:
            break

        q,r = divmod(x, prime)
        if r == 0:
            return False

    return True


def run():
    primes = [p for p in euler_util.primes(int(math.ceil(math.sqrt(987654321))))]

    max = 0
    toks = []
    for i in [1,2,3,4,5,6,7,8,9]:
        toks.append(i)
        for c in euler_util.combos(toks):
            x = euler_util.undigits(c)
            if is_prime(x, primes) and x > max:
                max = x

    # print max

run()
