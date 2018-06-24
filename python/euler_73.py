import fractions, math

import euler_util as eu

def run(max_d):
    sum = 0
    for den in xrange(3,max_d + 1):
        num = den * 3 / 7

        for num in xrange(den / 2, 0, -1):
            if eu.fraction_compare((num,den), (1,3)) <= 0:
                break
            if fractions.gcd(num, den) == 1:
                sum += 1

    return sum

if __name__ == '__main__':
    pass # print run(10000)
