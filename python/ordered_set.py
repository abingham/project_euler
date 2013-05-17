class OrderedSet(object):
    def __init__(self, data = None):
        if not data:
            self.data = []
        else:
            self.data = list(data)

    def add(self, value):
        if not value in self.data:
            self.data.append(value)

    def remove(self, value):
        return self.data.remove(value)

    def __getitem__(self, idx):
        return self.data[idx]

    def __delitem__(self, idx):
        del self.data[idx]

    def __len__(self):
        return len(self.data)
    
    def __contains__(self, value):
        return value in self.data

    def __repr__(self):
        return str(self.data)
