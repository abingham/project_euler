MAX_DIVISOR=20

def check(val):
    for i in range(MAX_DIVISOR,1,-1):
        if val % i != 0:
            return False
    return True

val = MAX_DIVISOR
while True:
    if check(val):
        break
    val += MAX_DIVISOR

print val
