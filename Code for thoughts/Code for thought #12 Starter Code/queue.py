### Code for thought #12
### In this assignment, we use the Queue class to implement a stack class named
### QueueStack. The class Queue is provided below. The __init__ method for
### QueueStack is already implemented. Note self._q is the only Queue object one
### can use to implement the methods for the class QueueStack. Moreover, one
### should not introduce any new variables other than an index used for loop in
### either push or pop methods.

class Queue:
    def __init__(self):
        self._L = []
		
    def enqueue(self, item):
    	self._L.append(item)
		
    def dequeue(self):
        return self._L.pop(0)
    
    def __len__(self):
        return len(self._L)
            
    def isempty(self):
        return len(self) == 0

class QueueStack:
    def __init__(self):
        self._q = Queue()
            
    def push(self, item):
        ### Add your code here
        self._q.enqueue(item)
        size = len(self._q) -1
        for i in range(size):
        	self._q.enqueue(self._q.dequeue())

    def pop(self):
        ### Add your code here
        return self._q.dequeue()


    def __len__(self):
        return len(self._q)

    def isempty(self):
        return len(self) == 0

def pushandpop(n):
    qstack = QueueStack()
    for i in range(n):
        qstack.push(i)
        print('push', i)

    print("Length of the stack:", len(qstack))
    
    while not qstack.isempty():
        print('pop', qstack.pop())

    print("Length of the stack:", len(qstack))

pushandpop(10)
