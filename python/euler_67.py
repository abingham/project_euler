def max_path(lattice):
    '''
    takes in a triangle lattice [[a],[b,c],[d,e,f],[g,h,i,j], ...]
    representing the graph:

                           a
                          b c
                         d e f
                        g h i j

    where the nodes are integers. This algorithm finds the path from
    the top level to the bottom which maximizes the sum of the nodes.

    The basic notion is to build up the sum from the bottom. For any
    node, if that node is in the maximal path, then the maximum of
    it's children will also be in the path. So, starting from the
    next-to-bottom row, replace each node's value with it's value
    plus the max of it's children. Then go to the next hightest level
    and do the same. Eventually, you'll reach the top and the only
    node in that row will contain the answer :)
    '''

    for row_idx in reversed(range(len(lattice) - 1)):
        row = lattice[row_idx]
        sub_row = lattice[row_idx + 1]
        for elem_idx in range(len(row)):
            row[elem_idx] += max(sub_row[elem_idx], sub_row[elem_idx + 1])
    return row[0]

def read_lattice(filename):
    result = []

    f = open(filename, 'r')
    for l in f:
        result.append([int(x) for x in l.split()])

    return result

def run():
    lattice = read_lattice('triangle.txt')
    return max_path(lattice)

# print run()
