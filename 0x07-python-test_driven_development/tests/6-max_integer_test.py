#!/usr/bin/python3
"""
Unittest for max_integer([...])

"""

import unittest
max_integer = __import__('6-max-integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Unittest for max_integer([...]).

    """
    def test_max_integer(self):
        # Test with a list of positive integers
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

        # Test with a list of positive integers in descending order
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

        # Test with a list of negative integers
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

        # Test with a list of negative integers in descending order
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)

        # Test with a list of positive and negative integers
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

        # Test with an empty list
        self.assertIsNone(max_integer([]))

        # Test with a list containing only one element
        self.assertEqual(max_integer([5]), 5)

        # Test with a list containing duplicate elements
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)

        # Test with a list containing float values
        self.assertEqual(max_integer([1.5, 2.7, 3.9]), 3.9)

if __name__ == '__main__':
    unittest.main()

