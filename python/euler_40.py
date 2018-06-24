sz = ''
for i in range(1,1000000):
    sz += str(i)
    if len(sz) >= 1000000:
        break

result = 1
for i in range(7):
    result *= int(sz[10**i - 1])

# print result
