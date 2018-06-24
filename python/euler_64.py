import math
import euler_util as eu

def test():
    sum = 0
    for i in range(14):
        if eu.is_square(i):
            continue
        cf = sqrt_continued_fraction(i)
        if len(cf) % 2 == 0:
            sum += 1
    assert sum == 4, 'there are only 4 matches for x <=13'

def run():
    sum = 0
    for i in range(10001):
        if eu.is_square(i):
            continue
        cf = eu.sqrt_continued_fraction(i)
        if len(cf) % 2 == 0:
            sum += 1
    return sum

test()
pass # §print run()
