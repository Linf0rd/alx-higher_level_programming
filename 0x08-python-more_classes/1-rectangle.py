#!/usr/bin/python3
"""
Defining a Rectangle object.
"""


class Rectangle:
    """
    Rectangle class that defines a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.

    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter method to retrieve the width of the rectangle.

        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method to set the width of the rectangle.

        Args:
            value (int): The width value to be set.

        Raises:
            TypeError: If the width is not an integer.
            ValueError: If the width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method to retrieve the height of the rectangle.

        """

    @height.setter
    def height(self, value):
        """
        Setter method to set the height of the rectangle.

        Args:
            value (int): The height value to be set,

        Raises:
            TypeError: If the height is not an integer.
            ValueError: If the height is less than 0.

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
