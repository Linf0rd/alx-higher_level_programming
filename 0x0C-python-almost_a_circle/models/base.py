#!/usr/bin/python3
"""
Defines the Base class.
"""
import json
import csv


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

    @classmethod
    def to_json_string(cls, list_dicts):
        """Return the JSON string representation of list_dictionaries."""
        if list_dicts is None or len(list_dicts) == 0:
            return "[]"
        return json.dumps(list_dicts)

    @classmethod
    def from_json_string(cls, json_str):
        """Return a list of dictionaries from a JSON string."""
        if json_str is None or len(json_str) == 0:
            return []
        return json.loads(json_str)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a list of instances to a JSON file."""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                dict_list = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(dict_list))

    @classmethod
    def load_from_file(cls):
        """Load a list of instances from a JSON file."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_str = file.read()
                dict_list = cls.from_json_string(json_str)
                return [cls.create(**d) for d in dict_list]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save a list of instances to a CSV file."""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline='') as file:
            csv_writer = csv.writer(file)
            for obj in list_objs:
                if cls.__name__ == 'Rectangle':
                    csv_writer.writerow(
                        [obj.id, obj.width, obj.height, obj.x, obj.y])
                elif cls.__name__ == 'Square':
                    csv_writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Load a list of instances from a CSV file."""
        filename = cls.__name__ + ".csv"
        instances = []
        try:
            with open(filename, "r", newline='') as file:
                csv_reader = csv.reader(file)
                for row in csv_reader:
                    if cls.__name__ == 'Rectangle':
                        d = {
                            'id': int(row[0]),
                            'width': int(row[1]),
                            'height': int(row[2]),
                            'x': int(row[3]),
                            'y': int(row[4])
                        }
                        instances.append(cls.create(**d))
                    elif cls.__name__ == 'Square':
                        d = {
                            'id': int(row[0]),
                            'size': int(row[1]),
                            'x': int(row[2]),
                            'y': int(row[3])
                        }
                        instances.append(cls.create(**d))
            return instances
        except FileNotFoundError:
            return []

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
