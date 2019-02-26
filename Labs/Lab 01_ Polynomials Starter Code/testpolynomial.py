import unittest
from polynomial import Monomial, Polynomial

class TestMonomial(unittest.TestCase):
    def testinit(self):
        Monomial(1,2)
        Monomial(1,0)
        Monomial(1,-1)

    def testeq(self):
        a = Monomial(1,2)
        b = Monomial(1.0, 2.0)
        c = Monomial(2,1)
        self.assertEqual(a, b)
        self.assertNotEqual(a,c)
        self.assertNotEqual(b,c)

    def testeqwithzero(self):
        self.assertEqual(Monomial(0,1), Monomial(0,3))

    def testlt(self):
        a = Monomial(2, 4)
        b = Monomial(3, 4)
        c = Monomial(2, 5)
        d = Monomial(3, 5)
        self.assertTrue(a < b)
        self.assertTrue(a < c)
        self.assertTrue(a < d)
        self.assertTrue(b < c)
        self.assertTrue(b < d)
        self.assertTrue(c < d)

    def testmul(self):
        a = Monomial(3,7)
        b = Monomial(2,11)
        c = Monomial(5,4)
        self.assertEqual(a * b, Monomial(6,18))
        self.assertEqual(b * a, Monomial(6,18))
        self.assertEqual(a * c, Monomial(15,11))
        self.assertEqual(c * b, Monomial(10,15))

    def testnegate(self):
        a = Monomial(-2, 2)
        b = Monomial(2, 2)
        c = Monomial(2,3)
        self.assertEqual(a, -b)
        self.assertEqual(b, -a)
        self.assertNotEqual(b, c)
        self.assertNotEqual(-a, c)

    def testevaluate(self):
        p = Monomial(2, 4)
        self.assertEqual(p.evaluate(-1), 2)
        self.assertEqual(p.evaluate(0), 0)
        self.assertEqual(p.evaluate(1), 2)
        self.assertEqual(p.evaluate(2), 32)
        # The following fails because of roundoff error:
        # self.assertEqual(p.evaluate(0.2), .0032)

    def testevaluateconstant(self):
        p = Monomial(5,0)
        self.assertEqual(p.evaluate(-5), 5)
        self.assertEqual(p.evaluate(0), 5)
        self.assertEqual(p.evaluate(1.2), 5)
        self.assertEqual(p.evaluate(10000), 5)

    def testevaluatedegenerate(self):
        p = Monomial(0, -1)
        self.assertEqual(p.evaluate(-10), 0)
        self.assertEqual(p.evaluate(0), 0)
        self.assertEqual(p.evaluate(3), 0)
        p = Monomial(0, -3)
        self.assertEqual(p.evaluate(0), 0)
        self.assertEqual(p.evaluate(2), 0)

class TestPolynomialEquality(unittest.TestCase):
    def testeq(self):
        a = Polynomial([(1,2), (2,3)])
        b = Polynomial([(2,3), (1,2)])
        self.assertEqual(a,b)

    def testeqwithzeros(self):
        a = Polynomial([(1,2), (0,3)])
        b = Polynomial([(0,4), (1,2)])
        self.assertEqual(a,b)

    def testeqwithseveralzeros(self):
        a = Polynomial([(0,12), (1,2), (0,3)])
        b = Polynomial([(0,4), (1,2)])
        self.assertEqual(a,b)

class TestPolynomial(unittest.TestCase):
    def testinit(self):
        Polynomial([(1,2)])
        Polynomial([(1,200000000000)])
        Polynomial([(1,2), (2,3)])
        a = Monomial(10, 5)
        b = Monomial(10, 15)
        Polynomial([a])
        Polynomial([a,b])
        Polynomial([a,b, (2,13)])

    def testevaluate(self):
        p = Polynomial([(1,2), (5,0)])
        self.assertEqual(p.evaluate(0), 5)
        self.assertEqual(p.evaluate(2), 9)

    def testevaluatebig(self):
        p = Polynomial([(2.4,100000)])
        self.assertEqual(p.evaluate(0), 0)
        self.assertEqual(p.evaluate(1), 2.4)

    def testmonomialextends(self):
        a = Monomial(1,2)
        self.assertTrue(isinstance(a, Monomial))

    def testeqmonomialispolywithoneterm(self):
        a = Monomial(3,7)
        b = Polynomial([(3,7)])
        c = Polynomial([a])
        self.assertEqual(a,b)
        self.assertEqual(a,c)
        self.assertEqual(b,c)

    def testadd(self):
        p = Polynomial([(1,2), (1,1), (1,0)])
        q = Polynomial([(2,2), (2,1), (2,0)])
        r = Polynomial([(0,0)])
        s = Polynomial([(3,4), (5,12)])
        t = Polynomial([(-1,1), (-1,0)])
        self.assertEqual(p + p, q)
        self.assertEqual(q + r, q)
        self.assertEqual(p + s, Polynomial([(1,0), (1,1), (1,2), (3,4), (5,12)]))
        self.assertEqual(p + t, Monomial(1,2))
        # Useful to include a negative test.
        self.assertNotEqual(p + s, t)

    def testmul(self):
        a = Polynomial([(1,1), (-1,0)]) # x - 1
        b = Polynomial([(2,1), (-3,0)]) # 2x - 3
        c = Polynomial([(2,2), (-5,1), (3,0)])
        self.assertEqual(a * b, c)

    def testmulmonomials(self):
        a = Monomial(10, 5)
        b = Monomial(3, 11)
        self.assertEqual(a*b, Polynomial([(30, 16)]))

    def testneg(self):
        a = Polynomial([(3,2), (1,1), (-1,0)]) # 3x^2 + x - 1
        nega = Polynomial([(-3,2), (-1,1), (1,0)])
        b = Polynomial([(2,1), (-3,0)]) # 2x - 3
        negb = Polynomial([(-2,1), (3,0)])
        self.assertEqual(-a, nega)
        self.assertEqual(-nega, a)
        self.assertEqual(-b, negb)
        self.assertEqual(-negb, b)
        self.assertEqual(-(-a),a)

    def testsub(self):
        p = Polynomial([(1,2), (1,1), (1,0)])
        q = Polynomial([(2,2), (2,1), (2,0)])
        r = Polynomial([(0,0)])
        s = Polynomial([(3,4), (5,12)])
        t = Polynomial([(-1,1), (-1,0)])
        u = Polynomial([(1,0), (1,1), (1,2), (3,4), (5,12)])
        self.assertEqual(q - p, p)
        self.assertEqual(q - r, q)
        self.assertEqual(u - s, p)
        self.assertEqual(u - p, s)
        self.assertEqual(p, Monomial(1,2) - t)
        # Useful to include a negative test.
        self.assertNotEqual(p - s, t)

    def testcall(self):
        p = Polynomial([(1,2), (5,0)])
        self.assertEqual(p(0), 5)
        self.assertEqual(p(2), 9)


if __name__ == '__main__':
    unittest.main()
