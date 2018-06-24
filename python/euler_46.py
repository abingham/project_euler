import euler_util

def twice_squares():
    for i in euler_util.numbers(1):
        yield 2 * (i**2)

def find_sum(x, ts, primes):
    ts.find(x)
    primes.find(x)

    for tsidx in range(len(ts)):
        curr_ts = ts[tsidx]
        if curr_ts >= x:
            return False
        diff = x - curr_ts
        if primes.find(diff) != -1:
            return True

    return False

def run():
    ts = euler_util.GenFinder(twice_squares())
    primes = euler_util.GenFinder(euler_util.gen_primes())

    for i in euler_util.numbers(9, 2):
        if primes.contains(i):
            continue

        if not find_sum(i, ts, primes):
            # print i
            return

run()
