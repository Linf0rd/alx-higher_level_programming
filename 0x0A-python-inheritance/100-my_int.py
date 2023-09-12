#!/usr/bin/python3
"""
Defining a class called MyInt that inherits from int.
"""


class MyInt(int):
    """
    A class called MyInt that inherits from int.
    """

    def __eq__(self, other):
        """
        Inverts the behaviour of the == operator.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverts the behavior of the != operator.
        """
        return super().__eq__(other)
