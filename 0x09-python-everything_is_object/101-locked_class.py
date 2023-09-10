#!/usr/bin/python3
"""
Locked class
"""

class LockedClass:
    """
    No attribute creation unless it is 'first_name'
    """

    __slots__ = ["first_name"]
