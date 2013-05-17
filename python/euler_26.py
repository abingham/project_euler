# find max cycle length in fractional part of 1/d for d < 1000

def cycle_length(den):
    history = []
    num = 1
    while True:
        try:
            idx = history.index(num)
            return len(history) - idx
        except:
            pass
        
        history.append(num)

        (d,m) = divmod(num, den)
        if m == 0:
            return 0
        num = m * 10

max_length = 0
max_idx = 1
for i in range(1,1000):
    l = cycle_length(i)
    if l > max_length:
        max_length = l
        max_idx = i

print max_idx,max_length
