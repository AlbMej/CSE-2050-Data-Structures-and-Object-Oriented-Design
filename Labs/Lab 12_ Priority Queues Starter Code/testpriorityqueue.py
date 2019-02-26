from priorityqueue import *
import unittest

class TestPriorityQueue(unittest.TestCase):
    def testinit(self):
        pq = PriorityQueue()
        ent1 = [[10, 'a', 100], [1, 'b', 10], [10, 'a', 99], [1, 'b', 1]]
        ent2 = [[1, 'b', 1], [1, 'b', 10], [10, 'a', 99], [10, 'a', 100]]
        pq = PriorityQueue(ent1)
        self.assertEqual(pq._entries, ent2)
        
    def testupheap(self):
        ent = [[10, 'p', 100], [1, 'q', 10], [10, 's', 99], [1, 'r', 1],
               [2, 'x', 6], [2, 't', 33], [10, 'z', 1000], [1000, 'w', 2]]
        res = [[100, 'c', 100], [10, 'p', 100], [10, 's', 99], [1, 'q', 10],
               [2, 'x', 6], [2, 't', 33], [10, 'z', 1000], [1000, 'w', 2], [1, 'r', 1]]
        pq = PriorityQueue(ent, lambda x:x[1])
        pq._entries.append([100, 'c', 100])
        pq._upheap(8)
        self.assertEqual(pq._entries, res)
        res = [[1000, 'a', 1], [100, 'c', 100], [10, 's', 99], [1, 'q', 10], [10, 'p', 100],
               [2, 't', 33], [10, 'z', 1000], [1000, 'w', 2], [1, 'r', 1], [2, 'x', 6]]
        pq._entries.append([1000, 'a', 1])
        pq._upheap(9)
        self.assertEqual(pq._entries, res)
        
    def testdownheap(self):
        ent = [[10, 'p', 100], [11, 'q', 10], [12, 's', 99], [13, 'r', 1],
               [14, 'x', 6], [15, 't', 33], [16, 'z', 1000], [17, 'w', 2]]
        res = [[11, 'q', 10], [13, 'r', 1], [12, 's', 99], [17, 'w', 2],
               [14, 'x', 6], [15, 't', 33], [16, 'z', 1000], [20, 'p', 100]]
        pq = PriorityQueue(ent, lambda x:x[0])
        pq._entries[0][0] = 20
        pq._downheap(0)
        self.assertEqual(pq._entries, res)
        pq._entries[0][0] = 18
        res = [[12, 's', 99], [13, 'r', 1], [15, 't', 33], [17, 'w', 2],
               [14, 'x', 6], [18, 'q', 10], [16, 'z', 1000], [20, 'p', 100]]
        pq._downheap(0)
        self.assertEqual(pq._entries, res)
        
    def testisheap(self):
        ent = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        pq = PriorityQueue(ent, lambda x:1 / x)
        pq._entries[3] = 2
        self.assertTrue(pq._isheap())
        pq._entries[3] = 7
        self.assertTrue(pq._isheap())
        pq._entries[3] = 10
        self.assertFalse(pq._isheap())
        pq._entries[3] = -1
        self.assertFalse(pq._isheap())
        
    def testupdate(self):
        ent = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        ent2 = [i + 20 for i in ent]
        pq1 = PriorityQueue(ent, lambda x:1 / x)
        pq2 = PriorityQueue(ent2)
        pq1.update(pq2)
        self.assertTrue(pq1._isheap())
        self.assertEqual(set(pq1._entries), set(ent + ent2))
        pq1 = PriorityQueue(ent, lambda x:1 / x)
        pq2.update(pq1)
        self.assertTrue(pq2._isheap())
        self.assertEqual(set(pq2._entries), set(ent + ent2))

if __name__ == '__main__':
    unittest.main()
