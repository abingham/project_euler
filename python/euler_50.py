import euler_util

def run():
    primes = [p for p in euler_util.primes(1000000)]
    print "primes calculated"

    sums = [0] + euler_util.accumulate(primes, 
                                       lambda x,y:x+y, 
                                       0)
    print "sums calculated"

    max_dist = 0
    max = 0
    for i in range(1, len(sums)):
        if len(sums) - max_dist <= 0:
            break
        for j in range(i + max_dist + 1, len(sums)):
            diff = sums[j] - sums[i-1]
            if diff >= 1000000:
                break
            if euler_util.bsearch(primes, diff) != -1:
                max_dist = (j - i) + 1
                max = diff
                print max, max_dist
    print "max =",max

def test():
    x = euler_util.accumulate([1,2,3], lambda x,y: x + y, 0)
    print x

run()
