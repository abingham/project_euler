# paths through a lattice

def pascals_triangle(depth):
    rval = [0] * depth
    rval[0] = 1
    work = rval[:]
    for i in range(1, depth):
        temp = work
        work = rval
        rval = temp
        for j in range(1, depth):
            rval[j] = work[j - 1] + work[j]
    return rval

pvals = pascals_triangle(41)
print pvals[19]
print pvals[20]
print pvals[21]



