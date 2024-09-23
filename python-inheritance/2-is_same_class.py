#!/usr/bin/python3
"""
Function that returns True if the object
is exactly an instance of the specified class
-otherwise False
"""


def is_same_class(obj, a_class):
    """
    Returns True if 'obj' is exactly an instance of 'a_class',
    otherwise returns False.

    Parameters:
    obj: The object to check.
    a_class: The class to compare against.
    """
    return type(obj) == a_class
