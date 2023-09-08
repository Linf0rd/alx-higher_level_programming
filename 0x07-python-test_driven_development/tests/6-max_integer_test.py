#!/usr/bin/python3
"""
Unittest for max_integer([...])

"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Unittest for max_integer([...]).

    """
    def test_max_integer(self):
        """ Test with a list of positive integers. """
        positive = [1, 2, 3, 4]
        self.assertEqual(max_integer(positive), 4)

    def test_positive_descending(self):
        """ Test with a list of positive integers in descending order. """
        positive_descending = [4, 3, 2, 1]
        self.assertEqual(max_integer(positive_descending), 4)

    def test_negative_integer(self):
        """ Test with a list of negative integers """
        negative = [-1, -2, -3, -4]
        self.assertEqual(max_integer(negative), -1)

    def test_negative_descending(self):
        """ Test with a list of negative integers in descending order. """
        negative_descending = [-4, -3, -2, -1]
        self.assertEqual(max_integer(negative_descending), -1)

    def test_positive_and_negative(self):
        """ Test with a list of positive and negative integers. """
        positive_and_negative = [-1, 2, -3, 4]
        self.assertEqual(max_integer(positive_and_negative), 4)

    def test_empty_list(self):
        """ Test with an empty list. """
        empty = []
        self.assertEqual(max_integer(empty), None)

        
    def test_one_element(self):
        """ Test with a list containing only one element. """
        one_element = [5]
        self.assertEqual(max_integer(one_element), 5)


    def test_duplicate_elements(self):
        """ Test with a list containing duplicate elements. """
        duplicate = [3, 3, 3, 3]
        self.assertEqual(max_integer(duplicate), 3)

    def test_floats(self):
        """ Test with a list containing float values. """
        floats = [1.5, 2.7, 3.9]
        self.assertEqual(max_integer(floats), 3.9)

if __name__ == '__main__':
    unittest.main()
