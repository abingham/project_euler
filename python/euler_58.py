# Counting primes on diagonal of spiral, looking for 'ring'
# where ratio of primes-on-diagonals to all-diagonals falls

import euler_util as eu
import prime_reader
import operator as op
import os

def side_length(ring):
    return ring * 2 - 1

def run():
    primes = prime_reader.read_primes_default()
    last_prime = primes.next()

    prime_count = 0
    diag_total = 1
    current = 1
    for ring in eu.numbers(2):
        incr = (ring - 1) * 2

        for corner in xrange(3):
            current = op.iadd(current, incr)
            while current > last_prime:
                last_prime = primes.next()
            if current == last_prime:
                prime_count = op.iadd(prime_count, 1)
            
        current = op.add(current, incr)
        
        diag_total = op.iadd(diag_total, 4)
        
        perc = op.div(float(prime_count), diag_total)

        # print ring, side_length(ring), last_prime, diag_total, perc
        
        if op.lt(perc, 0.1):
            return side_length(ring)

print run()
