#!/usr/bin/python3
"""
A base geometry class called BaseGeometry.
"""


class BaseGeometry:
    """
    A class called BaseGeometry with area and integer_validator methods.
    """

    def area(self):
        """
        Raises an Exception with the message "area() is no implemented."
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value to be an integer greater than 0.
        Raises TypeError or ValueError if the validation fails.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
