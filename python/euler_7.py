# 10001st prime

import euler_util

target_guess = 1000000
iter = euler_util.primes(target_guess)

for i in range(9999):
    iter.next()
print iter.next()
