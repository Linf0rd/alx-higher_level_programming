#!/usr/bin/python3
"""
Defining a class Rectangle that inherits from BaseGeometry.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class called Rectangle that inherits BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle object with width and height.
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
