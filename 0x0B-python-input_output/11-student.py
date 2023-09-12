#!/usr/bin/python3
"""
Define a class Student.
"""


class Student:
    """
    Represent a Student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Get a dictionary representation of the Student.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student.
        """
        for key, value in json.items():
            setattr(self, key, value)
