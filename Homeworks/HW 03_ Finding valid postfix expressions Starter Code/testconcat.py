import unittest
from twentyfour import concatenate

class Testconcat(unittest.TestCase):
    def testconcatenate(self):
        self.assertEqual(concatenate(3,7), 37)
        self.assertEqual(concatenate('5', '12'), 512)
        self.assertEqual(concatenate(13, 13), 1313)
        self.assertEqual(concatenate(11, 0), 110)

if __name__ == '__main__':
    unittest.main()