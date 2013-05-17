# sum of integers which are not the sum of abundant numbers

import euler_util

def abundant(x):
    return sum(euler_util.proper_divisors(x)) > x

def run():
    abundants = [i for i in range(12, 28123) if abundant(i)]
    ints = [False] * 28124
    for i in range(len(abundants)):
        for j in range(i, len(abundants)):
            sum = abundants[i] + abundants[j]
            if sum < len(ints):
                ints[sum] = True

    sum = 0
    for i in range(len(ints)):
        if not ints[i]:
            sum += i

    print sum

run()
