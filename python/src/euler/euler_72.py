import fractions

import euler_util as eu

primes = list(eu.primes(1000000))

def proper_fractions(den):
    return [num for num in xrange(1,den) if fractions.gcd(num,den) == 1]

def run(max):
    sum = 0
    for i in range(2, max + 1):
        sum += eu.eulers_totient(i)
    # print sum

if __name__ == '__main__':
    run(1000000)
