import euler_util

def complete(x):
    y = x[:]
    y.sort()
    return y == range(1, 10)

max_val = 0

for digits in euler_util.permutations(range(1,10), 4):
    base_value = euler_util.undigits(digits)

    for i in euler_util.numbers(2):
        curr_value = base_value * i
        digits += euler_util.digits(curr_value)
        if len(digits) > 9:
            break
        elif len(digits) == 9:
            if complete(digits):
                val = euler_util.undigits(digits)
                print base_value,i,val
                if val > max_val:
                    max_val = val
            break

print max_val
