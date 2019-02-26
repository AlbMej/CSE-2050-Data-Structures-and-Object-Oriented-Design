### Code for thought #13
### In this assignment, we implement the following class named
### SortedDoublyLinkedList. This class is very similar to DoublyLinkedList
### class. The difference is that all the data in a SortedDoublyLinkedList
### are sorted from the smallest to the largest. Implement the add method so
### that the data in the list are sorted.

class ListNode:
    def __init__(self, data, prev = None, link = None):
        self.data = data
        self.prev = prev
        self.link = link
        if prev is not None:
            self.prev.link = self
        if link is not None:
            self.link.prev = self

class SortedDoublyLinkedList:

    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0
    
    def _addbetween(self, item, before, after):
        node = ListNode(item, before, after)
        if after is self._head:
            self._head = node
        if before is self._tail:
            self._tail = node
        self._length += 1

    def add(self, item):
        ### Add your code here
        prev = None
        cur = self._head
        while cur and item > cur.data:
        	prev, cur = cur, cur.link
        self._addbetween(item,prev,cur)

    
    def __len__(self):
        return self._length

    def __str__(self):
        cur = self._head
        s = ''
        while cur:
            s += str(cur.data)
            s += ' '
            cur = cur.link
        s.rstrip()
        return s
    
def additems(n):    
    sdll = SortedDoublyLinkedList()
    for i in range(n):
        sdll.add(i)
    print(sdll)

additems(20)


"""
n = 10
sdll = SortedDoublyLinkedList()
for i in range(n):
  sdll.add(i)
print(str(sdll), '0 1 2 3 4 5 6 7 8 9 ')      

n = 10
sdll = SortedDoublyLinkedList()
for i in range(n-1, -1, -1):
  sdll.add(i)
print(str(sdll), '0 1 2 3 4 5 6 7 8 9 ')      

n = 5
sdll = SortedDoublyLinkedList()
for i in range(n):
  sdll.add(i)

for i in range(n-1, -1, -1):
  sdll.add(i)
print(str(sdll), '0 0 1 1 2 2 3 3 4 4 ')  """

