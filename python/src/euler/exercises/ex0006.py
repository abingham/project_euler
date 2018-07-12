"""
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10) ^ 2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def sum_of_squares(count):
    return sum(x*x for x in range(1, count+1))


def square_of_sum(count):
    return sum(range(1, count + 1)) ** 2


def main():
    return square_of_sum(100) - sum_of_squares(100)
