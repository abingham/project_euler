'''
P(n) = n(3n-1)/2

; sum must be pentagonal
P(s) = P(k) + P(j)
     = (k (3k - 1) / 2) + (j (3j - 1) / 2)
     = 

; difference must be pentagonal
P(d) = P(k) - P(j) 

; absolute value of difference is minimized
P(k) - P(j)
'''

import math
import euler_util as eu

class ComplexError:
    pass

def coeffs(x):
    r1, r2 = eu.quadratic_roots(3, -1, -2 * x)
    if r1.imag != 0:
        raise ComplexError()
    return r1, r2

def is_pentagonal(x):
    try:
        a,b = coeffs(x)
        if int(a.real) == a.real and a.real > 0:
            return True
        elif int(b.real) == b.real and b.real > 0:
            return True
        else:
            return False
    except ComplexError:
        return False

def run():
    ps = [eu.pentagonal(i) for i in xrange(1000000)]
    print 'done calculating pentagonals'

    min = None
    for j in xrange(1, 10000):
        print j
        for k in xrange(1, 10000):
            d = ps[k] - ps[j]
            
            if not min is None and (d > min):
                break

            if not is_pentagonal(d):
                continue
            
            s = ps[k] + ps[j]
            if not is_pentagonal(s):
                continue
            
            if d < min or min is None:
                min = d
            
    return min

def test():
    # print [(p, is_pentagonal(p)) for p in [eu.pentagonal(i) for i in xrange(10)]]
    print [(p, is_pentagonal(p)) for p in xrange(10)]

print run()
# test()
