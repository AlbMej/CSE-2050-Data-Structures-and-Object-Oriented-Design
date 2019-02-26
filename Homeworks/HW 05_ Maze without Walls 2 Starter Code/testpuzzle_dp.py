import unittest
from puzzle_dp import PuzzleDP

class TestPuzzleDP(unittest.TestCase):
    def testinit(self):
        PuzzleDP([[1] * 10] * 10)

    def testpathsolve(self):
        L = [[2,1,2],[9,9,2],[9,1,1]]
        p = PuzzleDP(L)
        self.assertEqual(p.pathsolve((0,0),(1,1)), [(0,0), (0,2), (2,2), (2,1),(1,1)])

    def testpathsolve_big(self):
        L = [[100000 for i in range(1000)] for j in range(1000)]
        L[0][0] = 5
        L[0][5] = 20
        L[20][5] = 10
        L[30][5] = 1
        L[29][5] = 100
        L[20][15] = 2
        L[29][105] = 5
        p = PuzzleDP(L)
        self.assertEqual(p.pathsolve((0,0), (29,100)), [(0,0), (0,5), (20,5),(30,5),(29,5),(29,105),(29,100)])
        self.assertEqual(p.pathsolve((0,0), (29,5)), [(0,0), (0,5), (20,5),(30,5),(29,5)])
        self.assertEqual(p.pathsolve((0,0), (30,6)), [(0,0), (0,5), (20,5),(30,5),(30,6)])
        self.assertEqual(p.pathsolve((0,5), (30,6)), [(0,5), (20,5),(30,5),(30,6)])

    def testreverse_simple(self):
        puz = PuzzleDP([[1] * 10] * 10)
        rev = puz.reverse()
        self.assertEqual(rev[3,4], {(2,4), (3,3), (3,5), (4,4)})
        self.assertEqual(rev[0,2], {(0,1), (0,3), (1,2)})
        self.assertEqual(rev[9,9], {(9,8), (8,9)})
        self.assertEqual(rev[0,0], {(0,1), (1,0)})

    def testreverse_tricky(self):
        puz = PuzzleDP([[5,4,3,2,1,9]])
        self.assertEqual(puz[0,2], 3)
        rev = puz.reverse()
        self.assertEqual(rev[0,5], {(0,i) for i in [0,1,2,3,4]})

    def testsolve_bigexample(self):
        L = [[1]*100]*100
        p = PuzzleDP(L)
        self.assertTrue(p.solve((0,0), (99,99)))
        self.assertTrue(p.solve((99,99),(0,0)))

if __name__ == '__main__':
    unittest.main()
