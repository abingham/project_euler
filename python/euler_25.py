import euler_util

target = 10**999
for (idx, f) in euler_util.fib():
    if f >= target:
        print idx
        break

        
