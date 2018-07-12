import euler_util

def curious(x, primes):
    for i in range(1,8):
        subnumber = euler_util.undigits(x[i:i+3])
        q,r = divmod(subnumber, primes[i - 1])
        if r != 0:
            return False
    return True

def run():
    primes = [p for p in euler_util.primes(17)]

    sum = 0
    for c in euler_util.combos(range(10)):
        if c[0] == 0:
            continue
        if curious(c, primes):
            # print c
            sum += euler_util.undigits(c)
    # print sum

def test():
    primes = [p for p in euler_util.primes(17)]
    # print curious(euler_util.digits(1406357289), primes)

run()
