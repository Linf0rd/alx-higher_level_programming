#!/usr/bin/python3
"""
Defining a function that adds attributes to objects.
"""


def add_attribute(obj, attribute, value):
    """
    Adds a new attribute to an objec if it's possible.
    Raises a TypeError if the object can't have a new attribute.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
