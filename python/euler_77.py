import euler_util as eu

def calc_value(primes, mults):
    sum = 0
    for idx,mult in enumerate(mults):
        sum += mult * primes[idx]
    return sum

def find_nonzero_multiplier(mults):
    for i,val in enumerate(mults):
        if val != 0:
            return i
    return len(mults)

def run(max_val):
    primes = list(eu.primes(max_val))
    mults = [0] * len(primes)
    counts = [0] * (max_val + 1)

    value = 0
    update_idx = 0
    while True:
        # calculate the current value
        # value = calc_value(primes, mults)

        if value <= max_val:
            counts[value] += 1
            mults[0] += 1
            value += 2
            continue

        # find first index that is not zero
        nzi = find_nonzero_multiplier(mults)
        if nzi == len(mults) - 1:
            break

        # zero it and everything before it out. Increment the next.
        for i in range(nzi + 1):
            mults[i] = 0
        mults[nzi + 1] += 1
        value = calc_value(primes, mults)

    for i,v in enumerate(counts):
        if v > 5000:
            # print i
            break

def main():
    run(100)

if __name__ == '__main__':
    main()
