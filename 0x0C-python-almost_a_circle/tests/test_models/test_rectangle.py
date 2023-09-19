#!/usr/bin/python3
"""Defines unittests for models/rectangle.py"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ Unittests for testing instances of the Rectangle class."""

    def test_constructor(self):
        r = Rectangle(10, 20, 2, 3, 4)
        self.assertEqual(r.id, 4)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)

    def test_getters_and_setters(self):
        r = Rectangle(10, 20, 2, 3, 4)
        r.width = 40
        r.height = 40
        r.x = 5
        r.y = 6
        self.assertEqual(r.width, 40)
        self.assertEqual(r.height, 40)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 6)

    def test_invalid_width(self):
        with self.assertRaises(TypeError):
            r = Rectangle("10", 20)
        with self.assertRaises(ValueError):
            r = Rectangle(-10, 20)

    def test_invalid_height(self):
        with self.assertRaises(TypeError):
            r = Rectangle(10, "20")
        with self.assertRaises(ValueError):
            r = Rectangle(10, -20)

    def test_invalid_x(self):
        with self.assertRaises(TypeError):
            r = Rectangle(10, 20, "2")
        with self.assertRaises(ValueError):
            r = Rectangle(10, 20, -2)

    def test_invalid_y(self):
        with self.assertRaises(TypeError):
            r = Rectangle(10, 20, 2, "3")
        with self.assertRaises(ValueError):
            r = Rectangle(10, 20, 2, -3)


if __name__ == '__main__':
    unittest.main()
