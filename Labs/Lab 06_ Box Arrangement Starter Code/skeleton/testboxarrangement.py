import unittest
from boxarrangement import *


class TestBoxArrangement(unittest.TestCase):

    def testboxinit(self):
        b = Box(10, 2, 4)
        self.assertEqual((b.length, b.width, b.height), (10, 2, 4))
        
    def testboxvolume(self):
        b = Box(10, 2, 4)
        self.assertEqual(b.volume(), 80)
        
    def testboxlessthan(self):
        b1 = Box(10, 2, 4)
        b2 = Box(2, 15, 3)
        self.assertTrue(b1 < b2)
        self.assertFalse(b2 < b1)
        
    def testboxequal(self):
        b1 = Box(10, 2, 4)
        b2 = Box(4, 5, 4)
        b3 = Box(1, 81, 1)
        self.assertTrue(b1 == b2)
        self.assertFalse(b1 == b3)
        
    def testboxlessthanequal(self):
        b1 = Box(10, 2, 4)
        b2 = Box(4, 5, 4)
        b3 = Box(1, 81, 1)
        self.assertTrue(b1 <= b2 <= b3)
        
    def testtruckinit(self):
        lst = [Box(1, 1, 1), Box(1, 2, 3), Box(2, 1, 3)]
        t = Truck(lst)
        self.assertEqual(t.boxes, lst)
        
    def testtrucksort(self):
        lst = [Box(1, 1, 1), Box(6, 1, 1), Box(1, 3, 1), Box(1, 2, 2), Box(5, 1, 1), Box(2, 1, 1)]
        t = Truck(lst)
        t.sort()
        self.assertEqual([b.volume() for b in t.boxes], [1, 2, 3, 4, 5, 6])
        t = Truck(lst)
        t.sort(key=lambda b: b.length // 2)
        self.assertEqual([b.length // 2 for b in t.boxes], [0, 0, 0, 1, 2, 3])
        t = Truck(lst)
        t.sort(key=lambda b: b.length + b.width)
        self.assertEqual([b.length + b.width for b in t.boxes], [2, 3, 3, 4, 6, 7])
        
    def testtrucksortbyvolume(self):
        lst = [Box(1, 1, 1), Box(6, 1, 1), Box(1, 3, 1), Box(1, 2, 2), Box(5, 1, 1), Box(2, 1, 1)]
        t = Truck(lst)
        t.sortbyvolume()
        self.assertEqual([b.volume() for b in t.boxes], [1, 2, 3, 4, 5, 6])
        
    def testtrucksortbylength(self):
        lst = [Box(1, 1, 1), Box(6, 1, 1), Box(1, 3, 1), Box(1, 2, 2), Box(5, 1, 1), Box(2, 1, 1)]
        t = Truck(lst)
        t.sortbylength()
        self.assertEqual([b.length for b in t.boxes], [1, 1, 1, 2, 5, 6])
        
    def testtrucksortbyheight(self):
        lst = [Box(1, 1, 2), Box(6, 1, 1), Box(1, 3, 4), Box(1, 2, 2), Box(5, 1, 6), Box(2, 1, 6)]
        t = Truck(lst)
        t.sortbyheight()
        self.assertEqual([b.height for b in t.boxes], [1, 2, 2, 4, 6, 6])
        
    def testtruckrotate(self):
        lst = [Box(1, 1, 1), Box(6, 1, 1), Box(1, 3, 1), Box(1, 2, 2),
               Box(2, 1, 2), Box(5, 1, 1), Box(2, 1, 1), Box(1, 2, 3)]
        t = Truck(lst)
        t.sort()
        t.rotate(0)
        self.assertEqual([b.volume() for b in t.boxes], [1, 2, 3, 4, 4, 5, 6, 6])
        t.rotate(8)
        self.assertEqual([b.volume() for b in t.boxes], [1, 2, 3, 4, 4, 5, 6, 6])
        t.rotate(3)
        self.assertEqual([b.volume() for b in t.boxes], [5, 6, 6, 1, 2, 3, 4, 4])
        t.rotate(1)
        self.assertEqual([b.volume() for b in t.boxes], [4, 5, 6, 6, 1, 2, 3, 4])
        t.rotate(-3)
        self.assertEqual([b.volume() for b in t.boxes], [6, 1, 2, 3, 4, 4, 5, 6])

        
if __name__ == '__main__':
    unittest.main()
