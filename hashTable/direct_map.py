class DirectAddressTable:
    def __init__(self, m):
        self.m = m
        self.table = [None] * m


    def set(self, key, value):
        if not (0 <= key < self.m):
            raise IndexError("key out of range for direct address table")
        self.table[key] = value


    def get(self, key):
        if not (0<= key < self.m):
            raise IndexError("key out of range for direct address table")
        return self.table[key]


    def delete(self, key):
        if not (0 <= key < m):
            raise IndexError("key out of range for direct address table")
        self.table[key] = None


    def contains(self, key):
        if not (0 <= key < self.m):
            return False
        return self.table[key] is not None
