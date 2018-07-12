class RingBuffer(object):
    def __init__(self, data = None):
        if not data:
            self.data = []
        else:
            self.data = list(data)

    def append(self, value):
        return self.data.append(value)

    def remove(self, value):
        return self.data.remove(value)

    def _normalize_index(self, idx):
        l = len(self.data)
        if l == 0:
            return IndexError()
        else:
            return divmod(idx, l)[1]

    def __getitem__(self, idx):
        return self.data[self._normalize_index(idx)]

    def __setitem__(self, idx, value):
        self.data[self._normalize_index(idx)] = value

    def __delitem__(self, idx):
        del self.data[self._normalize_index(idx)]

    def __len__(self):
        return len(self.data)

    def __contains__(self, value):
        return value in self.data

    def __repr__(self):
        return str(self.data)
