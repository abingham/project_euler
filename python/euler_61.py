import euler_util as eu
import operator as op

class Field:
    def __init__(self, vals):
        self.vals = vals
        self.free = True

def get_field(gen):
    val = 0
    rslt = []
    while val < 10000:
        val = gen.next()
        if val > 999:
            rslt.append(val)
    return rslt

def circle_match(x,y):
    return x % 100 == y / 100

def _solve(fields, result, result_index=1):
    for field in fields[1:]:
        if not field.free:
            continue

        field.free = False

        for val in field.vals:
            if circle_match(result[result_index - 1], val):
                result[result_index] = val
                if result_index == 5:
                    if circle_match(result[result_index], result[0]):
                        # print sum(result), result
                else:
                    _solve(fields, result, result_index + 1)

        field.free = True

def solve(fields, result):
    fields[0].free = False

    for val in fields[0].vals:
        result[0] = val
        _solve(fields, result)

def run():
    fields = [Field(get_field(g)) for g in [eu.triangles(), eu.squares(), eu.pentagonals(), eu.hexagonals(), eu.heptagonals(), eu.octagonals()]]
    solve(fields, [0] * 6)


# test()
run()
