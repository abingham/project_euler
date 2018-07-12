# how many lychrel numbers less than 10000

import euler_util as eu

def is_lychrel(x):
    digs = eu.digits(x)
    for i in range(49):
        rdigs = digs[:]
        rdigs.reverse()
        x += eu.undigits(rdigs)
        digs = eu.digits(x)
        if eu.palindrome(digs):
            return False
    return True

def run():
    return reduce(lambda x,y: x + 1 if is_lychrel(y) else x, range(1, 10000), 0)

def test():
    # print is_lychrel(349)
    pass

# print run()
#test()
