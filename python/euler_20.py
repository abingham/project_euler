def factorial(x):
    rval = 1
    while x > 1:
        rval *= x
        x -= 1
    return rval

f = factorial(100)
sum = 0
while f > 0:
    (f,m) = divmod(f, 10)
    sum += m
print sum
