# expansion of sqrt(2)

import euler_util as eu

def expand(count):
    num = 1
    den = 2
    for i in range(count - 1):
        num = 2 * den + num   # 2 + num / den
        (num,den) = (den,num) # swap...1 / (num / den)

    num += den

    return num,den

def topheavy(num, den):
    return eu.length(num) > eu.length(den)

def run_alt():
    # A less concise, perhaps more clear algorithm
    sum = 0
    for i in range(1, 1001):
        if topheavy(*expand(i)):
            sum += 1
    return sum

def run():
    return reduce(lambda x,y: x + 1 if topheavy(*expand(y)) else x,
                  range(1, 1001),
                  0)

def test():
    for i in range(1,9):
        pass # print i, expand(i)

# print run()
# print run_alt()
# test()
