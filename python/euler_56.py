# Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?

import euler_util as eu

def digital_sum(x):
    return sum(eu.digits(x))

def run():
    max = 0
    for a in range(100):
        for b in range(100):
            s = digital_sum(pow(a,b))
            if s > max:
                max = s

    return max

print run()
