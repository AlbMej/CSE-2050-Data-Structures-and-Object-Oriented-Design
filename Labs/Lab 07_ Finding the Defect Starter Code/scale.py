class Scale:
    def __init__(self, L):
        self._L = L

    def weigh(self, range1, range2):
        diff = sum(self._L[range1[0]:range1[1]])- sum(self._L[range2[0]:range2[1]])
        print(self._L[range1[0]:range1[1]], self._L[range2[0]:range2[1]])
        if(diff > 0):
            print(-1, "return")
            return -1
        elif(diff == 0):
            print(0, "return")
            return 0
        else:
            print(1, "return")
            return 1

    def __len__(self):
        return len(self._L)

    def __getitem__(self,item):
        return self._L[item]

    def __setitem__(self,index,value):
        self._L[index] = value
