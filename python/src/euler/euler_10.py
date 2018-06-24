# sum the primes beneath 2000000

import euler_util

max_candidate = 2000000

def slow():
    candidates = range(3, max_candidate, 2)
    primes = [2]
    while candidates[0] < (max_candidate / 2):
        print len(candidates), candidates[0]
        prime = candidates[0]
        primes.append(prime)
        candidates = filter(lambda x: x % prime != 0, candidates)
    primes += candidates
    print sum(primes)

def fast():
    sum = 0
    candidates = [True for i in range(max_candidate)]
    candidates[0] = False
    candidates[1] = False

    i = 0
    while i < len(candidates):
        if not candidates[i]:
            i += 1
            continue
        sum += i
        j = i
        while j < len(candidates):
            candidates[j] = False
            j += i
        i += 1
    print (sum)

def gen():
    sum = 0
    for p in euler_util.primes(max_candidate):
        sum += p
    print ( sum )

gen()
