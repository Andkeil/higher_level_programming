#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
       self.assertEqual(max_integer([1, 2, 3, 6]), 6)

    def test_withneg(self):
        self.assertEqual(max_integer([-1, 0, 64, 1, 2, 3, 4]), 64)

    def test_bool(self):
        self.assertEqual(max_integer([True, False, 17, 1, 2]), 17)

    def test_large(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5, 328908328108321883092183810]), 328908328108321883092183810)

    def test_maxbegin(self):
        self.assertEqual(max_integer([98, 1, 2, 3]), 98)

    def test_neg(self):
        self.assertEqual(max_integer([82, 1, 2, 3, 4 -2]), 82)

    def test_onlyneg(self):
        self.assertEqual(max_integer([-2, -1, -5, -6, -19]), -1)

    def test_oneelement(self):
        self.assertEqual(max_integer([3]), 3)

    def test_empty(self):
        self.assertIsNone(max_integer([]))

    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(max_integer([-1, 0, 54, 1, 2, "he", 4], 54))
    @unittest.expectedFailure
    def test_fail2(self):
        self.assertEqual(max_integer([-1, 0, 54, 1, 2, None, 4], 54))

if __name__ == '__main__':
    unittest.main()
