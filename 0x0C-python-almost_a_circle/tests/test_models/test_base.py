#!/usr/bin/python3
"""
Defines unittests for the Base class.
"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Defines the tests for the Base class.
    """

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_no_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_with_id(self):
        b2 = Base(12)
        self.assertEqual(b2.id, 12)

    def test_increment_id(self):
        b3 = Base()
        b4 = Base()
        self.assertEqual(b3.id, 1)
        self.assertEqual(b4.id, 2)

    def test_negative_id(self):
        b5 = Base(-1)
        self.assertEqual(b5.id, -1)

    def test_zero_id(self):
        b6 = Base(0)
        self.assertEqual(b6.id, 0)

    def test_string_id(self):
        b7 = Base("abc")
        self.assertEqual(b7.id, "abc")


if __name__ == "__main__":
    unittest.main()
