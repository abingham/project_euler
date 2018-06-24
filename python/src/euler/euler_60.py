from cPickle import dump,load
import sys

import euler_util as eu
import prime_reader

#reader = prime_reader.read_primes()
#primes = [reader.next() for i in range(10000000)]
primes = [p for p in eu.primes(100000000)]
# print 'primes generated'

def prime_pair(x,y):
    '''determine if x,y are a prime_pair, i.e. xy is prime and yx is
    prime'''

    if eu.bsearch(primes, eu.num_cat(x,y)) == -1:
        return False
    if eu.bsearch(primes, eu.num_cat(y,x)) == -1:
        return False
    return True

class Solution(object):
    def __init__(self):
        self.__soln = None
        self.__sum = 0

    def __set_soln(self, s):
        self.__soln = s
        self.__sum = sum(s)

    def __nonzero__(self):
        return self.__soln is not None

    soln = property(lambda x: x.__soln, __set_soln)
    sum = property(lambda x: x.__sum)

def solve(size, soln, candidates, rslt = []):
    if len(rslt) > 2:
        pass # print rslt

    for idx, cand in enumerate(candidates):
        if soln:
            if cand * (size - len(rslt)) + sum(rslt) > soln.sum:
                return

        r = rslt + [cand]

        if len(r) == size:
            # print '***',r
            if not soln or sum(r) < soln.sum:
                soln.soln = r
            return

        sub_candidates = filter(lambda x: prime_pair(x, cand),
                                candidates[idx + 1:])

        solve(size, soln, sub_candidates, r)

def run(size):
    soln = Solution()
    solve(size, soln, primes[1:2000])
    # print soln.soln, soln.sum

def test():
    build_pp_matrix(100)

def main():
    run(int(sys.argv[1]))

if __name__ == '__main__':
    # print len(primes)
    # test()
    main()
