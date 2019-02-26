class bigScale:
    def __init__(self, f, length):
        self.f = f
        self.length = length

    def __len__(self):
        return self.length

    def weigh(self, range1, range2):
        if(range1[0] > self.length or range1[1] > self.length):
            raise IndexError('index out of range')
        if(range1[0] < 0 or range2[1] < 0):
            raise IndexError('index out of range')
        diff = (range2[1] - range2[0] + self.f(range2)) - (range1[1] - range1[0] + self.f(range1))
        if(diff > 0):
            return 1
        if(diff == 0):
            return 0
        else:
            return -1
