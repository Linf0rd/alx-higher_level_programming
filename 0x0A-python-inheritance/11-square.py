#!/usr/bin/python3
"""
Defining a Rectangle subclass Square.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class called Square that inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a Square object with size.
        """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """
        Returns the string representation of the square.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
