def find_solutions(m,n,max):
    '''m > n

    a = 2mn
    b = m^2 - n^2
    c = m^2 + n^2
    '''

    rslt = []

    m_2 = m ** 2
    n_2 = n ** 2

    for k in xrange(1,max):
        a = k * 2 * m * n
        b = k * (m_2 - n_2)
        c = k * (m_2 + n_2)
        l = a + b + c
        if l > max:
            break
        if a > b:
            rslt.append((l, (b,a,c)))
        else:
            rslt.append((l, (a,b,c)))

    return rslt

def run(max):
    results = [[] for i in xrange(max + 1)]

    for n in xrange(1, max + 1):
        for m in xrange(n + 1, max + 1):
            solns = find_solutions(m,n,max)
            if len(solns) == 0:
                break
            for l,t in solns:
                if t not in results[l]:
                    results[l].append(t)

    return sum([1 for r in results if len(r) == 1])

if __name__ == '__main__':
    pass # print run(2000000)
