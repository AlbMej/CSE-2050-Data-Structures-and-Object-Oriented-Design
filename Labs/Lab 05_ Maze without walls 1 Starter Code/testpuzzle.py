import unittest
from puzzle import Puzzle

class TestPuzzle(unittest.TestCase):
    def testinit(self):
        Puzzle([[1]*10]*10) # square
        Puzzle([[1]*2]*4) # rectangle
        Puzzle([[1]*10]) # one row
        Puzzle([[1]]*10) # one column

    def testinitcheckforrect(self):
        with self.assertRaises(ValueError):
            Puzzle([[1,2], [1,2,3]])

    def testgetitem1(self):
        p = Puzzle([[i for i in range(21)]])
        self.assertEqual(p[0,4], 4)
        self.assertEqual(p[0,0], 0)
        self.assertEqual(p[0,20], 20)

    def testgetitem2(self):
        p = Puzzle([[i+(j*10) for i in range(10)] for j in range(10)])
        self.assertEqual(p[4,5], 45)
        self.assertEqual(p[0,0], 0)
        self.assertEqual(p[9,9], 99)
        self.assertEqual(p[9,0], 90)
        self.assertEqual(p[0,9], 9)

    def testrdsolve(self):
        p1 = Puzzle([[3,2,3,2],[4,0,2,4],[3,1,3,0],[2,2,5,0]])
        self.assertEqual(p1.rdsolve((0,0), (3,3)), False)
        self.assertEqual(p1.rdsolve((0,0), (2,3)), True)
        p2 = Puzzle([[1,2,3],[2,3,1],[3,1,0]])
        self.assertEqual(p2.rdsolve((0,0), (2,2)), True)
        self.assertEqual(p2.rdsolve((1,1), (2,0)), False)

    def testsolve(self):
        p1 = Puzzle([[3,2,3,2],[4,0,2,4],[3,1,3,0],[2,2,5,0]])
        self.assertEqual(p1.solve((0,0), (3,3)), True)
        self.assertEqual(p1.solve((0,0), (2,3)), True)
        self.assertEqual(p1.solve((0,2), (1,3)), False)
        p2 = Puzzle([[1,2,3],[2,3,1],[3,1,0]])
        self.assertEqual(p2.solve((0,0), (2,2)), True)
        self.assertEqual(p2.solve((1,1), (2,0)), False)
        self.assertEqual(p2.solve((2,1), (2,1)), True)

    def testsolve_manysolutions(self):
        p = Puzzle([[1] * 10] * 10)
        self.assertTrue(p.solve((0,0), (9,9)))
        self.assertTrue(p.rdsolve((0,0), (9,9)))
        self.assertTrue(p.solve((9,9), (0,0)))
        self.assertFalse(p.rdsolve((9,9), (0,0)))
        self.assertFalse(p.solve((0,0), (10,10)))

    def testsolve_bigexample(self):
        L = [[100000 for i in range(1000)] for j in range(1000)]
        L[0][0] = 5
        L[0][5] = 20
        L[20][5] = 10
        L[30][5] = 1
        L[29][5] = 100
        L[20][15] = 2
        L[29][105] = 5
        p = Puzzle(L)
        self.assertTrue(p.solve((0,0), (29,100)))
        self.assertFalse(p.solve((0,5), (20,20)))
        self.assertTrue(p.solve((20,5), (30,6)))
        self.assertFalse(p.solve((30,6), (20,5)))

if __name__ == '__main__':
    unittest.main()
