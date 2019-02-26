
class PriorityQueue:
    def __init__(self, entries=None, key=lambda x: x):
        self._entries = list(entries or [])
        self.key = key
        self._heapify()

    def __lt__(self, other):
        return self.key < other.key

    def insert(self, item):
        self._entries.append(item)
        self._upheap(len(self))

    def _parent(self, i):
        return (i - 1) // 2

    def _children(self, i):
        left, right = 2 * i + 1, 2 * i + 2
        return range(left, min(len(self), right + 1))
    
    def findtop(self):
        try:
            return self._entries[0]
        except:
            return None

    def removetop(self):
        L = self._entries
        if len(L) == 0:
            return None
        self._swap(0, len(L) - 1)
        item = L.pop()
        self._downheap(0)
        return item

    def _swap(self, a, b):
        L = self._entries
        L[a], L[b] = L[b], L[a]

    # implement this method 
    def _upheap(self, i):
        L = self._entries
        parent = self._parent(i)
        if i > 0 and self.key(L[i]) < self.key(L[parent]):
            self._swap(i,parent)
            self._upheap(parent)
    
    # implement this method
    def _downheap(self, i):
        L = self._entries
        children = self._children(i)
        if children:
            child = min(children, key = lambda x: self.key(L[x]))
            if self.key(L[child]) < self.key(L[i]):
                self._swap(i, child)
                self._downheap(child)

    def __len__(self):
        return len(self._entries)

    def _heapify(self):
        for i in range(len(self)):
            self._downheap(len(self) - i - 1)
    
    # implement this method
    def update(self, other):
        self._entries += other._entries 
        self._heapify()
        
    # implement this method
    def _isheap(self):
        #1 way: Finds the children of the current node and compares each child to the parent
        L = self._entries
        children = self._children(0)
        for i in range(len(self)):
            children = self._children(i)
            for child in children:
                parent = self._parent(child)
                if child > 0 and self.key(L[child]) < self.key(L[parent]): return False
        return True

    def _isheap(self):
        #Another way: Finds the parent of the current node and compares it to the current node(child)
        L = self._entries
        for i in range(1,len(self)):
            parent = self._parent(i)
            if i > 0 and self.key(L[i]) < self.key(L[parent]): return False
        return True



