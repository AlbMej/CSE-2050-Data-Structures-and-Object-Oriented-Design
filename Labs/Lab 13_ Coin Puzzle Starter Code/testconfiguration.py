import unittest
from configuration import Configuration

class TestConfiguration(unittest.TestCase):
    def testinit(self):
        Configuration((1,1,0,10,10))
        Configuration((1,1,1,0,10))
        Configuration((10,1,1,0,10))

    def testeq(self):
        a = Configuration((1, 1, 0, 10, 10))
        b = Configuration((1, 1, 0, 10, 10))
        c = Configuration((1, 1, 0, 10, 10, 1))
        d = Configuration((1, 10, 0, 10, 1))
        self.assertEqual(a,b)
        self.assertFalse(a == c)
        self.assertFalse(a == d)

    def testhash(self):
        a = Configuration((1, 1, 0, 10, 10))
        b = Configuration((1, 1, 0, 10, 10))
        self.assertEqual(hash(a), hash(b))
        self.assertEqual(len({a,b}), 1)

    def testmoves(self):
        c = Configuration((1,1,0,10,10))
        moves = set(c.moves())
        expected_tuples = [(1,0,1,10,10), (0,1,1,10,10),
                    (1,1,10,0,10), (1,1,10,10,0)]
        expected = {Configuration(t) for t in expected_tuples}
        self.assertEqual(moves, expected)

    def testmoves2(self):
        c = Configuration((0,1,1,10,10))
        moves = set(c.moves())
        expected_tuples = [(1,0,1,10,10), (1,1,0,10,10)]
        expected = {Configuration(t) for t in expected_tuples}
        self.assertEqual(moves, expected)

    def testmoves3(self):
        c = Configuration((1,0,1,10,10))
        moves = set(c.moves())
        expected_tuples = [(0,1,1,10,10), (1,1,0,10,10),(1,10,1,0,10)]
        expected = {Configuration(t) for t in expected_tuples}
        self.assertEqual(moves, expected)

    def testmoves4(self):
        c = Configuration((1,10,1,0))
        moves = set(c.moves())
        expected_tuples = [(1,10,0,1),(1,0,1,10)]
        expected = {Configuration(t) for t in expected_tuples}
        self.assertEqual(moves, expected)

    def testmoves5(self):
        c = Configuration((1,10,1,10,1,0,1))
        moves = set(c.moves())
        expected_tuples = [
        (1,10,1,10,0,1,1),
        (1,10,1,10,1,1,0),
        (1,10,1,0,1,10,1)]
        expected = {Configuration(t) for t in expected_tuples}
        self.assertEqual(moves, expected)


if __name__ == '__main__':
    unittest.main()
