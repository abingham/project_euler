# sum of diagonals on a spiral

sum = 1
current = 1

for ring in range(1, 501):
    for corner in range(1,5):
        current += 2 * ring
        sum += current

# print sum
