import math, sys
import euler_util as eu

def run(n):
    primes = list(eu.primes(int(math.ceil(math.sqrt(n)))))

    max_quotient = 0
    max_n = None

    for i in range(2,n + 1):
        phi = eu.eulers_totient(i, primes)
        rslt = float(i) / phi        

        if rslt > max_quotient:
            max_quotient = rslt
            max_n = i

    print max_n

def test():
    for i in range(2,11):
        et = eu.eulers_totient(i)
        print i, et, float(i) / et

def main():
    run(int(sys.argv[1]))

if __name__ == '__main__':
    main()
    #test()
