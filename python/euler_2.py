sum = 2
preva = 1
prevb = 2
while True:
    curr = preva + prevb
    if curr >= 4000000:
        break
    if curr % 2 == 0:
        sum += curr
    preva = prevb
    prevb = curr
print sum
