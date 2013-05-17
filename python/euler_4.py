import euler_util

min_val = 99
max_pal = 0
for i in range(999,min_val,-1):
    for j in range(i,min_val,-1):
        val = i * j
        if euler_util.palindrome(str(val)):
            if val > max_pal:
                print i,j,val
                min_val = j
                max_pal = val
