# triangle divisors

import euler_util

num_divisors = 500

def triangles():
    val = 1
    count = 1
    while True:
        yield val
        count += 1
        val += count

def triangle(i):
    val = 0
    for i in range(i + 1):
        val += i
    return val

def count_divisors(val):
    '''
    divisors can be calculated quickly by using the prime factorization
    '''
    pfactors = euler_util.prime_factors(val)
    return reduce(lambda x,y: x * y, [c + 1 for (f,c) in pfactors], 1)

def main():
    for t in triangles():
        num_div = count_divisors(t)
        print (t, num_div)
        if num_div > num_divisors:
            print (t)
            break

if __name__ == '__main__':
    main()
