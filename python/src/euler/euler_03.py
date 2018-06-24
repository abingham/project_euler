"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import euler.util

value = 600851475143

def main():
    return max([x[0] for x in euler.util.prime_factors(value)])
