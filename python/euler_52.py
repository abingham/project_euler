import euler_util, math

class Exc:
    pass

def run():
    for power in euler_util.numbers():
        start = 10**power
        cache = {}
        for i in range(start, int(math.ceil(10**(power + 1) / 6.0))):
            try:
                try:
                    base_digs = cache[i]
                except KeyError:
                    base_digs = euler_util.digits(i)
                    base_digs.sort()
                    cache[i] = base_digs

                for x in range(2, 7):
                    val = x * i
                    try:
                        digs = cache[val]
                    except KeyError:
                        digs = euler_util.digits(val)
                        digs.sort()
                        cache[val] = digs
                    if not digs == base_digs:
                        raise Exc

                # print i
                return
            except Exc:
                pass



run()
