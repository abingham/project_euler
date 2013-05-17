import euler_util as eu

def run(target=8):
    pgen = eu.GenFinder(eu.gen_primes())
    
    # Loop over all prime numbers
    for prime_idx in eu.numbers():
        curr_prime = pgen[prime_idx]
        curr_digits = eu.digits(curr_prime) # digits in current prime

        # Get all selections of indices from current digits
        for rindices in eu.selections(range(len(curr_digits))):
            rzero = 0 in rindices

            if len(rindices) == 0:
                continue

            found_primes = []
            work_digs = curr_digits[:] # copy digits of current prime

            # Choose the digit which we will insert at each index in rindices (the current selection)
            for replacement in range(10):
                if replacement == 0 and rzero:
                     continue

                for rindex in rindices:
                    work_digs[rindex] = replacement

                prime_idx = pgen.find(eu.undigits(work_digs))
                if prime_idx != -1:
                    found_primes.append(pgen[prime_idx])

            if len(found_primes) >= target:
                # print "answer =",min(found_primes),found_primes,rindices
                return min(found_primes)
       
def test():
    arr = [s for s in eu.selections(range(3))]
    arr.sort()
    print arr
         
print run()
# test()
                
