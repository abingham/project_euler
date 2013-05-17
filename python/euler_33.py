import euler_util

def equiv(a,b,c,d):
    return a * d == b * c

def alt(x):
    if x == 0:
        return 1
    else:
        return 0

def curious(a,b):
    if a % 10 == 0 and b % 10 == 0:
        return False
    
    a_digits = euler_util.digits(a)
    b_digits = euler_util.digits(b)
    for aidx in range(2):
        for bidx in range(2):
            if a_digits[aidx] == b_digits[bidx]:
                if equiv(a,b,a_digits[alt(aidx)],b_digits[alt(bidx)]):
                    return True
    return False

vals = []
for i in range(10,100):
    for j in range(i + 1, 100):
        if curious(i,j):
            vals.append((i,j))
print reduce(lambda x,y: x * y, [a for (a,b) in vals], 1)
print reduce(lambda x,y: x * y, [b for (a,b) in vals], 1) 

