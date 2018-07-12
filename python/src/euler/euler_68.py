import cStringIO, itertools, sys

from ordered_set import OrderedSet
from euler.lib.ring_buffer import RingBuffer

def rotate_solution(ring, externals):
    m = min(externals)
    while externals[0] != m:
        t = externals[0]
        del externals[0]
        externals.add(t)

        t = ring[0]
        del ring[0]
        ring.append(t)

    return ring, externals

def solution_to_string(ring, externals):
    ring, externals = rotate_solution(ring, externals)

    io = cStringIO.StringIO()
    for idx, e in enumerate(externals):
        io.write(str(e))
        io.write(str(ring[idx]))
        io.write(str(ring[idx + 1]))

    return io.getvalue()

def solve(ring, values):
    for value in values:
        soln = OrderedSet([value])
        target = value + ring[0] + ring[1]
        for ridx in range(1, len(ring)):
            diff = target - (ring[ridx] + ring[ridx + 1])
            # TODO: We could short-circuit here if diff is not in
            # values, but I like this flow better
            if diff in values:
                soln.add(diff)
        if len(soln) == len(values):
            return ring, soln
    return None

def run(size, target_string_size):

    solutions = []

    values = range(1, size * 2 + 1)
    for idx,v in enumerate(values[:-1 * (size - 1)]):
        for p in itertools.permutations(values[idx + 1:], size - 1):
            ring = RingBuffer([v] + list(p))
            soln = solve(ring,
                         [x for x in values if x not in ring])
            if soln:
                sz = solution_to_string(soln[0], soln[1])
                if len(sz) == target_string_size:
                    solutions.append(int(sz))

    # print max(solutions)

def main():
    run(int(sys.argv[1]), int(sys.argv[2]))

if __name__ == '__main__':
    main()
