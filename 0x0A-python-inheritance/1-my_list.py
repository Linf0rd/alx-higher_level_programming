#!/usr/bin/python3
"""
Creating Mylist class
"""


class MyList(list):
    """
    A class that inherits from list and provides additional functionality.
    """

    def print_sorted(self):
        """
        Prints the list in sorted order (ascending sort).
        """
        sorted_list = sorted(self)
        print(sorted_list)
