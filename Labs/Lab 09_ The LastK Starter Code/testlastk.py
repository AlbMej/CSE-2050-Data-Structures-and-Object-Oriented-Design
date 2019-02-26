from lastk import LastK
import unittest

class TestLastK(unittest.TestCase):
    """Tests for the LastK data structure."""

    def testinit(self):
        """Test the initializer. """
        t = LastK(5)
        t = LastK(4)

    def testadd(self):
        """Test add does not throw exceptions."""
        t = LastK(3)
        for i in [1,2,3,4,5,6,7,8]:
            t.add(i)

    def testgetitem(self):
        """Test __getitem__ works as expected."""
        t = LastK(4)
        for i in range(25):
            t.add(i)
        self.assertEqual(t[0], 21)
        self.assertEqual(t[1], 22)
        self.assertEqual(t[2], 23)
        self.assertEqual(t[3], 24)

    def testgetitemraisesindexerror(self):
        t = LastK(3)
        for i in range(5):
            t.add(i+4)
        with self.assertRaises(IndexError):
            t[3]
        s = LastK(100)
        for i in range(12):
            t.add(2*i)
        with self.assertRaises(IndexError):
            t[80]
        with self.assertRaises(IndexError):
            t[12]

    def testlen(self):
        k = 1000
        t = LastK(k)
        for i in range(k):
            self.assertEqual(len(t), i)
            t.add(i)
        for i in range(k):
            self.assertEqual(len(t), k)
            t.add(i)

    def testclear(self):
        t = LastK(10)
        for i in range(100):
            t.add(i*3+9)
        self.assertEqual(len(t), 10)
        t.clear()
        self.assertEqual(len(t), 0)

    def testfirst(self):
        t = LastK(3)
        t.add(1)
        self.assertEqual(t.first(), 1)
        t.add(3)
        self.assertEqual(t.first(), 1)
        t.add(5)
        self.assertEqual(t.first(), 1)
        t.add(7)
        self.assertEqual(t.first(), 3)
        t.add(9)
        self.assertEqual(t.first(), 5)

    def testfirstraiseserrronempty(self):
        t = LastK(10)
        with self.assertRaises(IndexError):
            t.first()

    def testlast(self):
        t = LastK(3)
        t.add(1)
        self.assertEqual(t.last(), 1)
        t.add(3)
        self.assertEqual(t.last(), 3)
        t.add(5)
        self.assertEqual(t.last(), 5)
        t.add(7)
        self.assertEqual(t.last(), 7)
        t.add(9)
        self.assertEqual(t.last(), 9)

    def testlastraiseserrronempty(self):
        t = LastK(10)
        with self.assertRaises(IndexError):
            t.last()


if __name__ == '__main__':
    unittest.main()
