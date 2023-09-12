#!/usr/bin/python3
"""
Creating a class.
"""


class BaseGeometry:
    """
    A class called BaseGeometry with an area method that raises an Exception.
    """

    def area(self):
        """
        Raises an Exception with the message"area() is not implemented".
        """
        raise Exception("area() is not implemented")
