import euler_util

def run():
    vals = []
    for i in range(1000000):
        if i == sum([d**5 for d in euler_util.digits(i)]):
            vals.append(i)
    # print vals
    # print sum(vals) - 1

def test():
    '''
    9**5 * x < 1.111111111111111 * (10**x)
    59049 * x < 1.111111111111111 * (10**x)
    53144.1 * x < 10**x
    '''
    for x in range(1,100):
        # print x
        if 53144.1 < (10**x) / x:
            break

#test()
run()
