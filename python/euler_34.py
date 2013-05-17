# 145 -> 1! + 4! + 5! = 145
# 8

import euler_util as eu

def curious(x):
    d = eu.digits(x)
    if len(d) == 1: return
    return sum([eu.fact(i) for i in d]) == x

def run():
    vals = []
    for i in range(1,10**7):
        if curious(i):
            vals.append(i)
    print sum(vals)

def test():
    for i in range(1,10):
        print i
        if eu.fact(9) * i < 10**i:
            print 'hmmm'
    
run()
