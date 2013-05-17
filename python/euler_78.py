import euler_util as eu
import numpy

cache = numpy.ndarray((100000), dtype='int')
cache.fill(-1)

# @eu.trace
def partitions(n):

    v = cache[n]
    if v != -1:
        return v

    if n < 0: return 0
    if n == 0: return 1

    sum = 0
    for k in xrange(1, n + 1):
        if (k + 1) % 2 == 0:
            a = 1
        else:
            a = -1

        b = n - (k * (3 * k - 1)) / 2
        c = n - (k * (3 * k + 1)) / 2

        if b < 0 and c < 0:
            break
        
        if b >= 0:
            sum += a * partitions(b)
        if c >= 0:
            sum += a * partitions(c)

    cache[n] = sum % 1000000
    return sum

def test():
    assert partitions(1) == 1
    assert partitions(2) == 2
    assert partitions(3) == 3
    assert partitions(4) == 5
    assert partitions(5) == 7
    assert partitions(6) == 11
    assert partitions(7) == 15
    assert partitions(8) == 22
    assert partitions(9) == 30
    assert partitions(10) == 42
    #assert partitions(100) == 190569292
    #assert partitions(200) == 3972999029388

def run():
    for n in eu.numbers():
        p = partitions(n)
        if p % 1000000 == 0:
            return n

if __name__ == '__main__':
    # test()
    print run()
