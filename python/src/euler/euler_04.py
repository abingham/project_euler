from euler.util import palindrome


def products(min_val, max_val):
    return (i * j
            for i in range(max_val, min_val - 1, -1)
            for j in range(i, min_val - 1, -1))

def main():
    return max(x
               for x in products(100, 999)
               if palindrome(str(x)))
