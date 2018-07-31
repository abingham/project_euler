"""The decimal number, 585 = 1001001001 (binary), is palindromic in both
bases.

Find the sum of all numbers, less than one million, which are palindromic in
base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)
"""

from euler.lib import util


def multi_palindrome(n):
    decimal = str(n)
    binary = '{:b}'.format(n)
    return util.palindrome(decimal) and util.palindrome(binary)


def main():
    return sum(n
               for n
               in range(1, 1000001)
               if multi_palindrome(n))
