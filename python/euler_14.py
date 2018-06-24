cache_size = 1000000
length_cache = [-1] * cache_size

def collatz_length_basic(val):
    if val == 1:
        return 1
    elif val % 2 == 0:
        return 1 + collatz_length(val / 2)
    else:
        return 1 + collatz_length(3 * val + 1)

def collatz_length(val):
    # print val
    if val < cache_size:
        if length_cache[val] != -1:
            # print 'cache hit'
            return length_cache[val]
        rval = collatz_length_basic(val)
        length_cache[val] = rval
    else:
        rval = collatz_length_basic(val)

    return rval

def full_problem():
    max = 0
    val = 0
    for i in range(1,1000000):
        cl = collatz_length(i)
        if cl > max:
            max = cl
            val = i

    print (max,val)

def pretend():
    print (collatz_length(13))

full_problem()
