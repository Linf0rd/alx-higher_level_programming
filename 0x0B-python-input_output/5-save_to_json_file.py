#!/usr/bin/python3
"""
Define a JSON file-writing function.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file using JSON
    """
    wih open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)
