# amicable numbers

# sums[a] == b
# sums[b] == a

import euler_util

sums = [0] + [sum(euler_util.proper_divisors(i)) for i in range(1,10000)]

amicable = set()
for a in range(1,10000):
    b = sums[a]
    if b == a:
        continue
    if b < 10000:
        if sums[b] == a:
            amicable.add(a)
            amicable.add(b)
    else:
        s = sum(euler_util.proper_divisors(b))
        if s == a:
            amicable.add(a)

# print sum(amicable)
