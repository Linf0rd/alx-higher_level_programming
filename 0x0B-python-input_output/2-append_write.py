#!/usr/bin/python3
"""
Defining a file-appending function.
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file (UTF8).
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        return file.write(text)
