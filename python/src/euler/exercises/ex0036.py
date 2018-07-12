import euler_util

sum = 0
for i in range(1000000):
    if euler_util.palindrome(str(i)) and euler_util.palindrome(euler_util.bin(i)):
        sum += i
# print sum
