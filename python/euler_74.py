import math

import euler_util as eu

# math.factorial(n)

def fact_sum(n):
    digs = eu.digits(n)
    return sum([math.factorial(x) for x in digs])

def pre_loop_length(n):
    vals = [n]
    
    while True:
        n = fact_sum(n)
        if n in vals:
            return len(vals)
        vals.append(n)

def run():
    count = 0
    for i in range(1000000):
        if i % 10000 == 0:
            print i

        l = pre_loop_length(i)
        if l == 60:
            count += 1
    return count

if __name__ == '__main__':
    print run()
