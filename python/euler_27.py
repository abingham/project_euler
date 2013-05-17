import euler_util

def f(n,a,b):
    return (n**2) + (a * n) + b

prime_gen = euler_util.gen_primes()
primes = [prime_gen.next() for i in range(1000)]

def count_primes(a,b):
    sum = 0
    for n in euler_util.numbers():
        val = f(n,a,b)
        while val > primes[-1]:
            primes.append(prime_gen.next())
        if not val in primes:
            return sum
        sum += 1

def run():
    max_count = 0
    max_a = 0
    max_b = 0

    for a in range(-999, 1000):
        for b in range(-999, 1000):
            count = count_primes(a,b)
            if count > max_count:
                max_count = count
                max_a = a
                max_b = b

    return (max_a, max_b, max_count)

result = run()
print result
print result[0] * result[1]
