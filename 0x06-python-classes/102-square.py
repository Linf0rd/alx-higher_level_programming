#!/usr/bin/python3
"""
Class Square that defines a square.
"""


class Square:
    """
    Class Square that defines a square.
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance.

        Args:
            size (float or int): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not a number.
            ValueError: If size is less than 0.

        """
        self.size = size

    @property
    def size(self):
        """
        Getter method to retrieve the size of the square,

        Returns:
            float or int: The size of the square,

        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size of the square.

        Args:
            value (float or int): The size of the square.

        Raises:
            TypeError: If size is not a number.
            ValueError: If size is less than 0.

        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            float or int: The area of the square.

        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Checks if the square area is equal to the area of another square.

        Args:
            other (Square): The other square to compare with,

        Returns:
            bool: True if the square areas are equal, False otherwise.

        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Checks if the square area is not equal to the area of another square.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the square areas are not equal, False otherwise.

        """
        return self.area() != other.area()

    def __gt__(self, other):
        """
        Checks if the square area is greater than the area of another square.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the square area is greater, False otherwise.

        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Checks if the square area is greater than or equal to the area of another square.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the square area is greater than or equal, False otherwise.

        """
        return self.area() >= other.area()

    def __lt__(self, other):
        """
        Checks if the square area is less than the area of another square.

        Args:
            other (Square): The other square to compare with,

        Returns:
            bool: True if the square area is less, False otherwise.

        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Checks if the square area is less than or equal to the area of another square.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the square area is less than or equal, False otherwise.

        """
        return self.area() <= other.area()
