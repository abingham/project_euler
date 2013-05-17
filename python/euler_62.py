import euler_util as eu

def run():
    data = {}
    for i in range(1, 10000):
        val = pow(i,3)

        nval = eu.digits(val)
        nval.sort()
        nval.reverse()
        nval = eu.undigits(nval)

        try:
            data[nval].append(val)
        except KeyError:
            data[nval] = [val]

    min = None
    for k,v in data.items():
        if len(v) == 5:
            if min is None or v[0] < min:
                min = v[0]
    return min

if __name__ == '__main__':
    print run()
