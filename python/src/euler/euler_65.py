# cf of e...[2;1,2,1,1,4,1,1,6,1,1,8,1,...,1,2k,1]

import euler_util as eu

def cf_e(i):
    if i == 0:
        return 2

    i -= 1

    d,m = divmod(i,3)
    if m == 0 or m == 2:
        return 1
    else:
        return 2 * (d + 1)

def convergent(cf):
    '''
    calculates the convergent represented by a continued fraction
    '''

    c = 1
    b = cf[-1]
    for a in reversed(cf[:-1]):
        b,c = (c,b)
        b = a * c + b
    return (b,c)

def run():
    which_convergent = 100
    cf = [cf_e(i) for i in range(which_convergent)]
    b,c = convergent(cf)
    # print sum(eu.digits(b))

def test():
    cf = []
    for i in range(0,10):
        cf.append(cf_e(i))
        # print i, convergent(cf)

# test()
run()
