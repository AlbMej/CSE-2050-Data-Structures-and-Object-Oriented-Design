import unittest
from organizedtruck import *
from boxarrangement import *
from intfunction import *
import random


class TestOrganizedTruck(unittest.TestCase):

    def testinit(self):
        lst = [Box(1, 1, 1), Box(1, 2, 3), Box(2, 1, 3)]
        tr = Truck(lst)
        ot = OrganizedTruck(tr)
        self.assertEqual(ot.truck.boxes, lst)

    def testiteratormultiple(self):
        lst = [Box(5, 1, 1), Box(1, 1, 1)]
        lstsorted = [Box(1, 1, 1), Box(5, 1, 1)]
        combination = []
        for box1 in lstsorted:
            for box2 in lstsorted:
                combination.append((box1, box2))
        tr = Truck(lst)
        ot = OrganizedTruck(tr)
        indx = 0
        for box1 in ot:
            for box2 in ot:
                self.assertEqual((box1, box2), combination[indx])
                indx += 1

    def testiterator(self):
        lst = [Box(5, 1, 1), Box(1, 2, 3), Box(6, 1, 1), Box(1, 1, 1), Box(1, 1, 1),
               Box(1, 1, 1), Box(2, 1, 1), Box(1, 3, 1), Box(1, 2, 2), Box(2, 1, 2)]
        result = [Box(1, 1, 1), Box(1, 1, 1), Box(1, 1, 1), Box(2, 1, 1), Box(1, 3, 1),
                Box(1, 2, 2), Box(2, 1, 2), Box(5, 1, 1), Box(1, 2, 3), Box(6, 1, 1)]
        tr = Truck(lst)
        ot = OrganizedTruck(tr)
        indx = 0
        for box1 in ot:
            self.assertEqual(box1, result[indx])
            indx += 1
            
    def testiteratortimecomplexity(self):
        num = 1000000
        repetition = 10
        tr = Truck(IntFunction(lambda i: Box(i // repetition, i // repetition, i // repetition), num))
        ot = OrganizedTruck(tr)
        otiter = iter(ot)
        prev = next(otiter)
        for item in otiter:
            self.assertTrue(item >= prev)
            prev = item

    def testgetitem(self):
        lst = [Box(5, 1, 1), Box(1, 2, 3), Box(6, 1, 1), Box(1, 1, 1),
               Box(2, 1, 1), Box(1, 3, 1), Box(1, 2, 2), Box(2, 1, 2)]
        tr = Truck(lst)
        ot = OrganizedTruck(tr)
        self.assertEqual(ot[3], Box(1, 1, 1))
        self.assertEqual(ot[6], Box(1, 2, 2))
        
    def testlen(self):
        lst = [Box(5, 1, 1), Box(1, 2, 3), Box(6, 1, 1), Box(1, 1, 1),
               Box(2, 1, 1), Box(1, 3, 1), Box(1, 2, 2), Box(2, 1, 2)]
        tr = Truck(lst)
        ot = OrganizedTruck(tr)
        self.assertEqual(len(ot), 8)
        lst.pop()
        self.assertEqual(len(ot), 7)
        lst.pop()
        self.assertEqual(len(ot), 6)        

    def testmin(self):
        lst = [Box(5, 1, 1), Box(1, 2, 3), Box(6, 1, 1), Box(1, 1, 1),
               Box(2, 1, 1), Box(1, 3, 1), Box(1, 2, 2), Box(2, 1, 2)]
        tr = Truck(lst)
        ot = OrganizedTruck(tr)
        self.assertEqual(ot.min(), Box(1, 1, 1))
        tr.rotate(2)
        self.assertEqual(ot.min(), Box(1, 1, 1))
        tr.rotate(3)
        self.assertEqual(ot.min(), Box(1, 1, 1))
        tr.rotate(-6)
        self.assertEqual(ot.min(), Box(1, 1, 1))

    def testmin2(self):
        lst = [Box(5, 1, 1), Box(1, 5, 1), Box(5, 1, 1), Box(5, 1, 1),
               Box(1, 5, 1), Box(1, 1, 5), Box(1, 2, 1)]
        tr = Truck(lst)
        ot = OrganizedTruck(tr)
        self.assertEqual(ot.min(), Box(1, 2, 1))
        
    def testmintimecomplexity(self):
        num = 1000000000
        repetition = 10
        tr = Truck(IntFunction(lambda i: 
                               Box(abs(i - num) // repetition, abs(i - num) // repetition, abs(i - num) // repetition)
                               , num))
        ot = OrganizedTruck(tr)
        self.assertEqual(ot.min(), Box(0, 0, 0))

    def testmax(self):
        lst = [Box(5, 1, 1), Box(1, 2, 3), Box(6, 1, 1), Box(1, 1, 1),
               Box(2, 1, 1), Box(1, 3, 1), Box(1, 2, 2), Box(2, 1, 2)]
        tr = Truck(lst)
        ot = OrganizedTruck(tr)
        self.assertEqual(ot.max().volume(), 6)
        tr.rotate(2)
        self.assertEqual(ot.max().volume(), 6)
        tr.sort()
        self.assertEqual(ot.max().volume(), 6)

    def testmax2(self):
        lst = [Box(1, 1, 1), Box(1, 2, 1), Box(3, 1, 1), Box(1, 2, 2),
               Box(2, 2, 1), Box(1, 5, 1), Box(1, 2, 3), Box(7, 1, 1), Box(1, 7, 1)]
        tr = Truck(lst)
        ot = OrganizedTruck(tr)
        self.assertEqual(ot.max().volume(), 7)
        tr.rotate(-3)
        self.assertEqual(ot.max().volume(), 7)
        tr.rotate(4)
        self.assertEqual(ot.max().volume(), 7)
        
    def testmaxtimecomplexity(self):
        num = 1000000000
        repetition = 10
        tr = Truck(IntFunction(lambda i: Box(i // repetition, i // repetition, i // repetition), num))
        ot = OrganizedTruck(tr)
        self.assertEqual(ot.max(), Box(num // repetition - 1, num // repetition - 1, num // repetition - 1))

    def testsearch(self):
        lst = [Box(1, 1, 1), Box(1, 1, 1), Box(1, 1, 1), Box(1, 2, 1), Box(3, 1, 1), Box(1, 2, 2),
               Box(2, 2, 1), Box(4, 1, 1), Box(1, 5, 1), Box(1, 2, 3), Box(1, 6, 1), Box(7, 1, 1), Box(1, 7, 1)]
        tr = Truck(lst)
        tr.rotate(4)
        ot = OrganizedTruck(tr)
        self.assertEqual([b.volume() for b in ot.search(Box(2, 2, 1))], [4, 4, 4])
        self.assertEqual([b.volume() for b in ot.search(Box(1, 1, 6))], [6, 6])
        self.assertEqual([b.volume() for b in ot.search(Box(1, 1, 1))], [1, 1, 1])
        self.assertEqual(ot.search(Box(1, 1, 0)), None)
        self.assertEqual(ot.search(Box(1, 4, 3)), None)
        tr.rotate(4)
        self.assertEqual([b.volume() for b in ot.search(Box(2, 2, 1))], [4, 4, 4])
        self.assertEqual([b.volume() for b in ot.search(Box(1, 1, 6))], [6, 6])
        self.assertEqual([b.volume() for b in ot.search(Box(2, 1, 1))], [2])
        
    def testsearchtimecomplexity(self):
        num = 1000000000
        repetition = 10
        tr = Truck(IntFunction(lambda i: Box(i // repetition, i // repetition, i // repetition), num))
        ot = OrganizedTruck(tr)
        key = random.randint(0, num // repetition - 1)
        self.assertEqual([b.volume() for b in ot.search(Box(key, key, key))], [key ** 3 for i in range(repetition)])
        key = random.randint(0, num // repetition - 1)
        self.assertEqual([b.volume() for b in ot.search(Box(key, key, key))], [key ** 3 for i in range(repetition)])
        key = random.randint(0, num // repetition - 1)
        self.assertEqual([b.volume() for b in ot.search(Box(key, key, key))], [key ** 3 for i in range(repetition)])
        key = random.randint(0, num // repetition - 1)
        self.assertEqual([b.volume() for b in ot.search(Box(key, key, key))], [key ** 3 for i in range(repetition)])
        key = random.randint(0, num // repetition - 1)
        self.assertEqual([b.volume() for b in ot.search(Box(key, key, key))], [key ** 3 for i in range(repetition)])


if __name__ == '__main__':
    unittest.main()
