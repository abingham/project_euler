import euler_util

def run():
    primes = euler_util.GenFinder(euler_util.primes(9999))

    for i in range(1000,10000 - (3330 * 2)):
        if not primes.contains(i):
            continue

        j = i + 3330
        if not primes.contains(j):
            continue

        k = j + 3330
        if not primes.contains(k):
            continue

        idigs = euler_util.digits(i)
        idigs.sort()

        jdigs = euler_util.digits(j)
        jdigs.sort()

        if not idigs == jdigs:
            continue

        kdigs = euler_util.digits(k)
        kdigs.sort()
        if not kdigs == idigs:
            continue

        match = [i,j,k]
        match.sort()
        # print match

run()
