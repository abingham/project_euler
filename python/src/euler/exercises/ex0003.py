"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import euler.lib.primes
value = 600851475143

def main():
    return max(euler.lib.primes.prime_factors(value))
