# how many sundays on first of month in [1/1/1901, 12/31/2000]

months = [
    31, # jan
    28, # feb
    31, # mar
    30, # apr
    31, # may
    30, # jun
    31, # jul
    31, # aug
    30, # sept
    31, # oct
    30, # nov
    31 # dec
    ]

def is_leap_year(y):
    if y % 4 == 0:
        if y % 100 != 0 or y % 400 == 0:
            return True
        else:
            return False
    else:
        return False

def month_length(m, y):
    if m == 1: # feb is special
        if is_leap_year(y):
            return months[m] + 1
        else:
            return months[m]
    else:
        return months[m]

count = 0
curr_day = 1 # jan. 1, 1900 is a monday

# incr past 1900
for m in range(len(months)):
    curr_day += month_length(m, 1900)
    curr_day %= 7

for y in range(1901,2001):
    for m in range(len(months)):
        if curr_day == 0:
            count += 1
        curr_day += month_length(m, y)
        curr_day %= 7

print count
        
        
