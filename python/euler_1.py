sum = 0
i = 0
while True:
    i += 3
    if i < 1000:
        sum += i
    else:
        break

i = 0
while True:
    i += 5
    if i < 1000:
        sum += i
    else:
        break
    i += 5
    if i < 1000:
        sum += i
    else:
        break
    i += 5
    # ignore

print sum
    
