# for x^2 - Dy^2 = 1 (quadratic Diophantine, Pell's equation),
# minimize x for given values of D

import euler_util as eu

def solves_pell(x,y,d):
    # determines if x,y,d are a solution to Pell
    return (pow(x,2) - d * pow(y,2)) == 1

def pell_min_x(d):
    '''
    for a given d, this find a solution to Pell (x,y) that
    minimizes x.
    '''
    cf = eu.sqrt_continued_fraction(d)
    tail_len = len(cf) - 1

    x,y = eu.convergent(cf[:1])
    if solves_pell(x,y,d):
        return (x,y)

    while True:
        for i in range(len(cf) - 1):
            x,y = eu.convergent(cf[:-1 * (tail_len - i)])
            if solves_pell(x,y,d):
                return (x,y)
        cf += cf[-1 * tail_len:]

def max_x(max_d):
    '''
    for all d <= max_d, this finds the d for which the
    solution to Pell (x,y) minimizing x is maximal in x.
    '''

    max = 0
    rslt = None
    for d in range(2,max_d + 1):
        if eu.is_square(d):
            continue
        x,y = pell_min_x(d)
        if x > max:
            max = x
            rslt = d

    return rslt

def test():
    assert max_x(7) == 5, 'Test failed.'

def run():
    return max_x(1000)

test()
# print run()
