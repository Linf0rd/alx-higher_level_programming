#!/usr/bin/python3
"""
A function that returns the same class or inherits from a class.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if the object is an instance of, or if the object is an instance
    of a class that inherited from, the specified class.
    """
    return isinstance(obj, a_class)
