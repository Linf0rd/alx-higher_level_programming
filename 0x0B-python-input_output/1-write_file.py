#!/usr/bin/python3
"""
Defining a file-writing function.
"""


def write_file(filename="", text=""):
    """ Write a string to a text file (UTF8).
    """
    with open(filename, mode='w', encoding='utf8') as file:
        return file.write(text)
