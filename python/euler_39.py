max_solutions = 0
max_size = 0
for p in range(120, 1001):
    sum = 0
    for c in range(1, p - 1):
        c2 = c**2
        for a in range(1, (p - c) / 2):
            b = p - (a + c)
            if a**2 + b**2 == c2:
                sum += 1
    if sum > max_solutions:
        max_solutions = sum
        max_size = p
        print max_size,'->',max_solutions

print 'MAX:',max_size,'->',max_solutions
    
