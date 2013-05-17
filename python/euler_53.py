import euler_util

def build_factorials(count=100):
    rval = [1] * (count + 1)
    for i in range(2, count + 1):
        rval[i] = rval[i - 1] * i
    return rval

facts = build_factorials()

def combos(n, r):
    return facts[n] / (facts[r] * facts[n - r])

def run():
    sum = 0
    for n in range(23, 101):
        rgen = euler_util.numbers(1, 1, n + 1)
        try:
            while combos(n, rgen.next()) <= 1000000:
                pass
            sum += 1
            while combos(n, rgen.next()) > 1000000:
                sum += 1
        except StopIteration:
            pass
    print sum

def test():
    print combos(5,3)

run()
    
