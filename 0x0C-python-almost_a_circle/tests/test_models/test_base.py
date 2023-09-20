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

    def test_base_auto_id(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, obj2.id - 1)

    def test_base_custom_id(self):
        obj = Base(89)
        self.assertEqual(obj.id, 89)

    def test_to_json_string_with_none(self):
        result = Base.to_json_string(None)
        self.assertIsNotNone(result)

    def test_to_json_string_with_empty_list(self):
        result = Base.to_json_string([])
        self.assertIsNotNone(result)

    def test_to_json_string_with_list(self):
        data = [{"id": 12}]
        result = Base.to_json_string(data)
        self.assertIsInstance(result, str)

    def test_from_json_string_exists(self):
        self.assertTrue(hasattr(Base, "from_json_string"))

    def test_from_json_string_with_empty_string(self):
        result = Base.from_json_string("[]")
        self.assertIsInstance(result, list)

    def test_from_json_string_with_string(self):
        data = '[{ "id": 89 }]'
        result = Base.from_json_string(data)
        self.assertIsInstance(result, list)


if __name__ == "__main__":
    unittest.main()
