from nim import Nim
from gametree import GameTree
from TicTacToe import TicTacToe
import unittest

class TestGameTree(unittest.TestCase):
    """Tests for the GameTree data structure"""

    def testinit(self):
        """Test the initializer"""
        n1 = Nim([2,3,4])
        g1 = GameTree(n1)
        n2 = Nim([3,1,4,2])
        g2 = GameTree(n2)

    def testcurrentwins(self):
        """Test currentwins()"""
        n1 = Nim([2,3,4])
        g1 = GameTree(n1)
        self.assertEqual(g1.currentwins(), True)
        n2 = Nim([1,0,1])
        g2 = GameTree(n2)
        self.assertEqual(g2.currentwins(), True)
        n3 = Nim([1,0,1,1])
        g3 = GameTree(n3)
        self.assertEqual(g3.currentwins(), False)

    def testcurrentloses(self):
        """Test currentloses()"""
        n1 = Nim([2,3,4])
        g1 = GameTree(n1)
        self.assertEqual(g1.currentloses(), False)
        n2 = Nim([1,0,1])
        g2 = GameTree(n2)
        self.assertEqual(g2.currentloses(), False)
        n3 = Nim([1,0,1,1])
        g3 = GameTree(n3)
        self.assertEqual(g3.currentloses(), True)
    
    def testcurrentdraws(self):
        """Test currentdraws()"""
        n1 = Nim([1,0,1])
        g1 = GameTree(n1)
        self.assertEqual(g1.currentdraws(), False)
        n2 = Nim([1,0,1,1])
        g2 = GameTree(n2)
        self.assertEqual(g2.currentdraws(), False)

    def testtictactoewins(self):
        """Test currentloses() on TicTacToe"""
        t1 = TicTacToe('X', 'OO_XX____')
        g1 = GameTree(t1)
        self.assertEqual(g1.currentwins(), True)
        t3 = TicTacToe('X', 'X__X__O_O')
        g3 = GameTree(t3)
        self.assertEqual(g3.currentwins(), False)
        t3 = TicTacToe('O', '____X____')
        g3 = GameTree(t3)
        self.assertEqual(g3.currentwins(), False)

    def testtictactoeloses(self):
        """Test currentwins() on TicTacToe"""
        t1 = TicTacToe('X', 'OO_XX____')
        g1 = GameTree(t1)
        self.assertEqual(g1.currentloses(), False)
        t3 = TicTacToe('X', 'X__X__O_O')
        g3 = GameTree(t3)
        self.assertEqual(g3.currentloses(), True)
        t3 = TicTacToe('O', '____X____')
        g3 = GameTree(t3)
        self.assertEqual(g3.currentloses(), False)


    def testtictactoedraws(self):
        t1 = TicTacToe('X', 'OO_XX____')
        g1 = GameTree(t1)
        self.assertEqual(g1.currentdraws(), False)
        t3 = TicTacToe('X', 'X__X__O_O')
        g3 = GameTree(t3)
        self.assertEqual(g3.currentdraws(), False)
        t3 = TicTacToe('O', '____X____')
        g3 = GameTree(t3)
        self.assertEqual(g3.currentdraws(), True)
        t4 = TicTacToe('X', 'XOOOXXX__')
        g4 = GameTree(t4)
        self.assertEqual(g4.currentwins(), True)

if __name__ == '__main__':
    unittest.main()