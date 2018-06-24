# pythagorean triplets
max_val = 1000

for a in range(max_val):
    for b in range(a + 1, max_val):
        for c in range(b + 1, max_val):
            sum = a + b + c
            if sum == 1000 and a**2 + b**2 == c**2:
                pass # print a,b,c,a * b * c
            elif sum > 1000:
                break
