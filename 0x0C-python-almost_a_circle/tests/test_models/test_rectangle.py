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

class TestRectangleCreation(unittest.TestCase):
    """Unittests for creating Rectangle instances with different numbers of arguments."""

    def test_rectangle_creation_2_args(self):
        try:
            rect = Rectangle(1, 2)
        except Exception as e:
            self.fail(f"Failed to create Rectangle(1, 2): {e}")

    def test_rectangle_creation_3_args(self):
        try:
            rect = Rectangle(1, 2, 3)
        except Exception as e:
            self.fail(f"Failed to create Rectangle(1, 2, 3): {e}")

    def test_rectangle_creation_4_args(self):
        try:
            rect = Rectangle(1, 2, 3, 4)
        except Exception as e:
            self.fail(f"Failed to create Rectangle(1, 2, 3, 4): {e}")



if __name__ == '__main__':
    unittest.main()
