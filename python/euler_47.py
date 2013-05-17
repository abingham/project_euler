import euler_util

def run():
    vals = []

    for i in euler_util.numbers(1):
        factors = [p for p in euler_util.prime_factors(i)]
        if len(factors) == 4:
            vals.append(i)
            print vals
            if len(vals) == 4:
                print vals
                return
        else:
            vals = []

run()
