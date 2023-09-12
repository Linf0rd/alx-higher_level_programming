#!/usr/bin/python3
"""
Returns only sub class of a class
"""


def inherits_from(obj, a_class):
    """
    Checks if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
