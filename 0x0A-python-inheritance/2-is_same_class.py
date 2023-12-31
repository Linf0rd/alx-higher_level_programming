#!/usr/bin/python3
"""
Return true if the object is an instance of a class.
"""


def is_same_class(obj, a_class):
    """
    Checks if the object is exactly an instance of the specified class.
    """
    return type(obj) is a_class
