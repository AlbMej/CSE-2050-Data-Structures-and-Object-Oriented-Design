import unittest
from cipher import Cipher

class TestCipher(unittest.TestCase):
    def testcreate(self):
        c = Cipher("BCDEFGHIJKLMNOPQRSTUVWXYZA")

    def testencode(self):
        c = Cipher("BCDEFGHIJKLMNOPQRSTUVWXYZA")
        self.assertEqual(c.encode("DEF"), "EFG")
        self.assertEqual(c.encode("AAAB"), "BBBC")
        self.assertNotEqual(c.encode("ABC"), "ABC")

    def testdecode(self):
        c = Cipher("BCDEFGHIJKLMNOPQRSTUVWXYZA")
        self.assertEqual(c.decode("CDE"), "BCD")
        self.assertEqual(c.decode("ZZZAB"), "YYYZA")
        self.assertNotEqual(c.decode("ABC"), "ABC")

    def testencodewithextras(self):
        c = Cipher("JMBCYEKLFDGUVWHINXRTOSPZQA")
        self.assertEqual(c.encode("ABC, DE::"), "JMB, CY::")
        self.assertEqual(c.encode("   ZWV#$!"), "   APS#$!")
        self.assertEqual(c.encode("1234567..."), "1234567...")

    def testdecodewithextras(self):
        c = Cipher("JMBCYEKLFDGUVWHINXRTOSPZQA")
        self.assertEqual(c.decode("JMB, CY::"), "ABC, DE::")
        self.assertEqual(c.decode("   APS#$!"), "   ZWV#$!")
        self.assertEqual(c.decode("1234567..."), "1234567...")

    def testencodewithlowercase(self):
        c = Cipher("JMBCYEKLFDGUVWHINXRTOSPZQA")
        self.assertEqual(c.encode("Abc, De::"), "JMB, CY::")
        self.assertEqual(c.encode("   zwv#$!"), "   APS#$!")
        self.assertNotEqual(c.encode("   APS#$!"), "   APS#$!")

    def testdecodewithlowercase(self):
        c = Cipher("JMBCYEKLFDGUVWHINXRTOSPZQA")
        self.assertEqual(c.decode("jMb, cy::"), "ABC, DE::")
        self.assertEqual(c.decode("   Aps#$!"), "   ZWV#$!")

    def testcreatecipherfromcodeword(self):
        c = Cipher("A")
        self.assertEqual(c.encode("ABCDEF"), "AZYXWV")
        c = Cipher("CBA")
        self.assertEqual(c.encode("HELLO"), "VYRRO")

if __name__ == '__main__':
    unittest.main()
