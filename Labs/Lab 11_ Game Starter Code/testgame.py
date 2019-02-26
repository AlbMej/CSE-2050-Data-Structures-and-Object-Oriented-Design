from nim import Nim
from gametree import GameTree
import unittest

class TestNim(unittest.TestCase):
    """Tests for the Nim data structure"""

    def testinit(self):
        """Test the initializer"""
        n = Nim([2,3,4])
        n = Nim([1,1,1])
        n = Nim([2,3,4,5,6])

    def testisover(self):
        """Test isover()"""
        n = Nim([2,3,4])
        self.assertEqual(n.isover(), False)
        n = Nim([2,0,1])
        self.assertEqual(n.isover(), False)
        n = Nim([0,1,0])
        self.assertEqual(n.isover(), True)

    def testmoves(self):
        """Test moves()"""
        n = Nim([1,2,1])
        nmoves = n.moves()
        moveslist = []
        for mv in nmoves:
            moveslist.append(mv.rows)
        truelist = [[0,2,1],[1,1,1],[1,0,1],[1,2,0]]
        self.assertTrue(sorted(moveslist) == sorted(truelist))

class TestGameTree(unittest.TestCase):
    """Tests for the GameTree data structure"""

    def testinit(self):
        """Test the initializer"""
        n1 = Nim([2,3,4])
        g1 = GameTree(n1)
        n2 = Nim([3,1,4,2])
        g2 = GameTree(n2)

if __name__ == '__main__':
    unittest.main()