class Matrix:
    def __init__(self, rows, cols, default=None):
        self.data = [[default for j in range(cols)] for i in range(rows)]
        self._cols = cols

    def get(self, row, col):
        return self.data[row][col]

    def set(self, row, col, val):
        self.data[row][col] = val

    def __repr__(self):
        rval = ''
        for r in xrange(len(self.data)):
            row = self.data[r]
            for c in xrange(len(row)):
                rval += '%s' % self[r][c] + '\t'
            rval += '\n'

        return rval

    rows = property(lambda x: len(x.data))
    cols = property(lambda x: x._cols)

class SparseMatrix:
    def __init__(self, default=None):
        self.default = default
        self.data = {}
        self._cols = 0
        self._rows = 0

    def get(self, row, col):
        try:
            return self.data[row][col]
        except KeyError:
            return self.default

    def set(self, row, col, x):
        try:
            r = self.data[row]
        except KeyError:
            if row >= self._rows:
                self._rows = row + 1
            if col >= self._cols:
                self._cols = col + 1
            self.data[row] = { col : x }
            return

        if col >= self._cols:
            self._cols = col + 1
        r[col] = x

    rows = property(lambda x : x._rows)
    cols = property(lambda x : x._cols)

def test_template(m):
    # print m.get(1,2)
    m.set(1,2,3)
    # print m.get(1,2)
    # print m.rows, m.cols

    try:
        pass # print m.get(42,69)
    except IndexError:
        pass

    try:
        m.set(69,42,2001)
    except IndexError:
        pass

def test_dense():
    m = Matrix(10,10)
    test_template(m)

def test_sparse():
    m = SparseMatrix()
    test_template(m)

if __name__ == '__main__':
    test_dense()
    test_sparse()
