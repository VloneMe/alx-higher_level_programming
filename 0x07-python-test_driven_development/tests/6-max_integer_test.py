#!/usr/bin/python3
"""
write unittests for the function def max_integer(list=[]):.
"""

import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Unit tests for the max_integer function.
    """

    def test_max_integer(self):
        """
        Test for a normal list of positive integers.
        """
        test_list = [1, 2, 3, 8, 4]
        self.assertEqual(max_integer(test_list), max(test_list))

    def test_max_integer_neg(self):
        """
        Test for a list of positive and negative integers.
        """
        test_list = [1, 2, 3, 8, 4, -40, -400, -12, 0]
        self.assertEqual(max_integer(test_list), max(test_list))

    def test_max_integer_float(self):
        """
        Test for a list of positive and negative floating-point numbers.
        """
        test_list = [1.3, 2.34, 3.12, 8.536, 4.6, -40.0, -400.999, -12.6, 0]
        self.assertEqual(max_integer(test_list), max(test_list))

    def test_max_integer_empty(self):
        """
        Test for an empty list.
        """
        test_list = []
        self.assertIsNone(max_integer(test_list))

    def test_max_integer_one(self):
        """
        Test for a list with a single element.
        """
        test_list = [3]
        self.assertEqual(max_integer(test_list), max(test_list))

    def test_max_integer_first(self):
        """
        Test for a list where the first element is the maximum.
        """
        test_list = [5, 1, 4, 2]
        self.assertEqual(max_integer(test_list), max(test_list))

    def test_max_integer_last(self):
        """
        Test for a list where the last element is the maximum.
        """
        test_list = [1, 4, 2, 4, 4, 4, 9]
        self.assertEqual(max_integer(test_list), max(test_list))

if __name__ == '__main__':
    unittest.main()
