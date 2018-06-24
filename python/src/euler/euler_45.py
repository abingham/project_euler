import euler_util

def run():
    t = euler_util.triangles()
    for i in range(285):
        t.next()

    p = euler_util.pentagonals()
    curr_p = p.next()

    h = euler_util.hexagonals()
    curr_h = h.next()

    while True:
        curr_t = t.next()

        while curr_p < curr_t:
            curr_p = p.next()

        while curr_h < curr_t:
            curr_h = h.next()

        if curr_t == curr_h and curr_t == curr_p:
            # print curr_t
            return

run()
