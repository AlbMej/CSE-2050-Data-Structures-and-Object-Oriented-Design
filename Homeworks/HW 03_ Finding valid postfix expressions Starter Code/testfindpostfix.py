import unittest
from twentyfour_hw import *

class TestPostfix(unittest.TestCase):
    
    def testevaluatewithconcat(self):
        a = Postfix_Expression("AAAJ")
        b = Postfix_Expression("8833")
        c = Postfix_Expression("63J8")
        self.assertEqual(a.evaluate("JA+AA%c"), 120)
        self.assertEqual(a.evaluate("386Ac%*"), 24)
        self.assertEqual(a.evaluate("JAAcA%*"), 0)
        self.assertEqual(a.evaluate("63cJ-8/"), 6.5)
        self.assertEqual(a.evaluate("J74*c6/"), 188)

    def testfindpostfix(self):
        pexp = Postfix_Expression("AAJA")
        result = {"A A + J A + *"}
        self.assertEqual(find_postfix(pexp, "AAJA"), result)

        pexp = Postfix_Expression("AKKJ")
        result = {"A K % K J + *", "A K % K * J +"}
        self.assertEqual(find_postfix(pexp, "AKKJ"), result)

        pexp = Postfix_Expression("9998")
        self.assertEqual(find_postfix(pexp, "9998"), set())

        pexp = Postfix_Expression("Q777")
        result = {"Q 7 7 + 7 / *", "Q 7 7 7 + / /", "Q 7 / 7 7 + *", "Q 7 7 + * 7 /"}
        self.assertEqual(find_postfix(pexp, "Q777"), result)

        pexp = Postfix_Expression("75A0")
        result = {"7 5 / A + 0 *", "7 5 * A 0 + -", "7 5 * A - 0 -"}
        self.assertEqual(find_postfix(pexp, "75A0"), result)

if __name__ == '__main__':
    unittest.main()
