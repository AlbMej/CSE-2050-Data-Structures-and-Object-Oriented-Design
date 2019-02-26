class LastK:
    def __init__(self,k):
    	self.k = k
    	self.data = []
    	self.start_index = 0

    def add(self, item):
    	if len(self) == self.k:
    		self.data[self.start_index] = item
    		self.start_index = (self.start_index + 1) % self.k
    	else:
    		self.data.append(item)

    def __getitem__(self,i):
    	if i < 0 or i >= len(self): raise IndexError
    	if len(self) == self.k: return self.data[(i+1) % self.k]
    	return self.data[i]

    def first(self):
    	if len(self.data) == 0: raise IndexError
    	return self.data[self.start_index]

    def last(self):
    	if len(self.data) == 0: raise IndexError
    	return self.data[(self.start_index + len(self) - 1)% self.k]

    def clear(self):
    	del self.data[:]

    def __len__(self):
    	return len(self.data)

c = LastK(4)
for i in range(1,6):
	c.add(i)
print(c[0])