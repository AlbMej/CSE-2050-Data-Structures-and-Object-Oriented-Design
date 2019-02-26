import unittest
from scale import Scale
from bigScale import bigScale
from defects import defects
import random

class TestDefects(unittest.TestCase):

    def testsmall(self):
        L = [1,1,1,1,2,1,1,1]
        self.assertEqual(defects(Scale(L)), L.index(2))
        L2 = [1,1,1,1,2,1,1,1,1]
        self.assertEqual(defects(Scale(L2)), L2.index(2))
        L3 = [10,10,10,10,20,10,10,10,10]
        self.assertEqual(defects(Scale(L3)), L3.index(20))

    def testbig(self):
        tests = 10
        size = 1000000000
        for j in range(tests):
            defect = random.randint(0, size+j)
            s2 = bigScale(lambda i: i[0] <= defect < i[1], size+j)
            self.assertEqual(defects(s2), defect)

if __name__ == '__main__':
    unittest.main()
