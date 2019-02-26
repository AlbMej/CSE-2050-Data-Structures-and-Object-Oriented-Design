import unittest
from coinpuzzle import CoinPuzzle
from configuration import Configuration

class TestCoinPuzzle(unittest.TestCase):
    def testpath11(self):
        p = CoinPuzzle(1,1)
        a = Configuration((1,0,10))
        b = Configuration((10,1,0))
        path = p.solve(a,b)
        self.assertEqual(len(path),3)
        for i in range(len(path) - 1):
            self.assertTrue(path[i+1] in list(path[i].moves()))

    def testpath22(self):
        p = CoinPuzzle(2,2)
        a = Configuration((1,1,0,10,10))
        b = Configuration((10,10,0,1,1))
        path = p.solve(a,b)
        self.assertEqual(len(path),9)
        #Check that the path is valid
        for i in range(len(path) - 1):
            self.assertTrue(path[i+1] in list(path[i].moves()))
        # Check that there are no shortcuts
        for i in range(len(path) - 2):
            self.assertTrue(path[i+2] not in list(path[i].moves()))

    def testpath13(self):
        p = CoinPuzzle(1,3)
        a = Configuration((0,1,10,10,10))
        b = Configuration((1,10,10,0,10))
        path = p.solve(a,b)
        self.assertEqual(len(path),3)
        for i in range(len(path) - 1):
            self.assertTrue(path[i+1] in list(path[i].moves()))

    def testpathmultiplecalls(self):
        p = CoinPuzzle(4,3)
        a = Configuration((1,1,1,1,0,10,10,10))
        b = Configuration((1,1,1,1,10,0,10,10))
        c = Configuration((1,1,1,1,10,10,10,0))
        for i in range(100):
            p.solve(a,b)
        self.assertEqual(len(p.solve(b,c)), len(p.solve(c,b)))
        self.assertEqual(len(p.solve(a,c)), 3)
        self.assertEqual(len(p.solve(c,a)), 3)

    def testpathspeedtest(self):
        p = CoinPuzzle(4,3)
        a = Configuration((1,1,1,1,10,0,10,10))
        b = Configuration((1,1,1,1,10,10,10,0))
        for i in range(10000):
            p.solve(a,b)


if __name__ == '__main__':
    unittest.main()
