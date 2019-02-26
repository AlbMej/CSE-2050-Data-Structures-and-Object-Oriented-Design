import unittest
from twentyfour import Postfix_Expression

class TestPostfix(unittest.TestCase):
    def testinit(self):
        Postfix_Expression("AAAJ")
        Postfix_Expression("8833")
        Postfix_Expression("63J8")

    def testisvalid(self):
        a = Postfix_Expression("AAAJ")
        b = Postfix_Expression("8833")
        c = Postfix_Expression("63J8")
        self.assertEqual(a.isvalid("AAA-*J/"), True)
        self.assertEqual(a.isvalid("8/8-/33"), False)
        self.assertEqual(a.isvalid("00/0-/9"), False)
        self.assertEqual(a.isvalid("638J-*+"), True)

    def testevaluate(self):
        a = Postfix_Expression("AAAJ")
        b = Postfix_Expression("8833")
        c = Postfix_Expression("63J8")
        self.assertEqual(a.evaluate("JA+AA%-"), 12)
        self.assertEqual(a.evaluate("8383/-/"), 24)
        self.assertEqual(a.evaluate("JAA+A%*"), 0)
        self.assertEqual(a.evaluate("63*J-7/"), 1)
        self.assertEqual(a.evaluate("J83**6/"), 44)

if __name__ == '__main__':
    unittest.main()
