import unittest
from polynomial import Monomial, Polynomial

class TestNewton(unittest.TestCase):
    def testlinear(self):
        p = Polynomial([(1,1), (-1,0)])
        self.assertTrue(abs(p.root() - 1) < 0.001)
        p = Polynomial([(1,1), (3,0)])
        self.assertTrue(abs(p.root() + 3) < 0.001)
        p = Polynomial([(4,1), (-8,0)])
        self.assertTrue(abs(p.root() - 2) < 0.001)

    def testquadratic1(self):
        p = Polynomial([(1,2)])
        self.assertTrue(abs(p.root() - 0) < 0.001)

    def testquadratic2(self):
        root = -4
        linear = Polynomial([(1,1), (-root,0)])
        p = linear * linear
        self.assertTrue(abs(p.root() - root) < 0.001)

    def testquadratic3(self):
        root = 13.12
        linear = Polynomial([(1,1), (-root,0)])
        p = linear * linear
        self.assertTrue(abs(p.root() - root) < 0.001)

    def testhighdegree(self):
        root = 10
        p = Polynomial([(1,1), (-root,0)])
        for i in range(2):
            p = p * p
        result = p.root()
        print(result - root)
        self.assertTrue(abs(result - root) < .02)

        # Should do better with a good guess.
        result = p.root(11)
        print(result - root)
        self.assertTrue(abs(result - root) < .01)

        # Should do even better with more iterations.
        result = p.root(11, 1000)
        print(result - root)
        self.assertTrue(abs(result - root) < .002)

    def testhighdegree2(self):
        roots = [2, -4, 5, 8, -1]        
        p=Polynomial([(1,0)])
        for poly in [Polynomial([(1, 1), (-i, 0)]) for i in roots]:
            p*=poly
        for r in roots:
            self.assertTrue(abs(p.root(r-1) - r) < .001)


if __name__ == '__main__':
    unittest.main()
