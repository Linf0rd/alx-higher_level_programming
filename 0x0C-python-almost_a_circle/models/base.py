#!/usr/bin/python3
"""
Defines the Base class.
"""
import json


class Base:
    """This is he Base class for managing id attribute."""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class.

        Args:
            id (int): The ID of the instance. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write JSON string representation of list_objs to a file."""
        if list_objs is None:
            list_objs = []
            filename = cls.__name__ + ".json"
            with open(filename, "w") as file:
                json_str = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
                file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """Return the list of dictionaries represented by json_string."""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create and return an instance with attributes from dictionary."""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            dummy_instance = cls()
        dummy_instance.update(**dictionary)
        return dummy_instance


    @classmethod
    def load_from_file(cls):
        """Load instances from a JSON file and return a list of instances."""
        file_name = cls.__name__ + ".json"
        try:
            with open(file_name, 'r') as file:
                json_str = file.read()
                json_list = cls.from_json_string(json_str)
                instances = [cls.create(**d) for d in json_list]
                return instances
            except FileNotFoundError:
                return []
