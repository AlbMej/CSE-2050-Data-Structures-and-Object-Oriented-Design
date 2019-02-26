import unittest
from polynomial import Monomial, Polynomial

class TestPrimes(unittest.TestCase):
    def testmonmialprime(self):
        a = Monomial(12, 4)
        self.assertEqual(a.prime(), Monomial(48,3))
        self.assertEqual(a.prime().prime(), Monomial(144,2))

    def testconstantprime(self):
        a = Monomial(12, 0)
        self.assertEqual(a.prime(), Monomial(0,0))

    def testpolynomialprime(self):
        p = Polynomial([(1,2), (3,1), (5,0)])
        q = Polynomial([(2,1), (3,0)])
        r = Polynomial([(2,0)])
        zero = Monomial(0,0)
        self.assertEqual(p.prime(), q)
        self.assertEqual(q.prime(), r)
        self.assertEqual(r.prime(), zero)

    def testpolynomialconstantprime(self):
        p = Polynomial([(1,0)])
        zero = Monomial(0,0)
        self.assertEqual(p.prime(), zero)
        q = Polynomial([(2,0), (5,0)])
        self.assertEqual(q.prime(), zero)

    def testunorderednonreducedpolynomials(self):
        p=Polynomial([(1,0),(3,2),(5,6),(0,2),(2,1),(6,2)])
        self.assertEqual(p.prime().reduce(), Polynomial([(2,0),(18,1),(30,5)]))

if __name__ == '__main__':
    unittest.main()
