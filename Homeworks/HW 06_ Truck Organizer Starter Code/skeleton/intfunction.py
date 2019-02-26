class IntFunction:
    def __init__(self, f, length):
        self._f = f
        self._length = length

    def __getitem__(self, k):
        if isinstance(k, slice):
            start = k.start or 0
            step = k.step or 1
            stop = k.stop or len(self)
            return [self[i] for i in range(start, stop, step)]
        if k != int(k):
            raise TypeError('indices must be integers')
        if k < 0:
            k = len(self) + k
        if k < 0 or k >= len(self):
            raise IndexError('index out of range')
        return self._f(k)

    def __iter__(self):
        for i in range(len(self)):
            yield self[i]

    def __len__(self):
        return self._length
