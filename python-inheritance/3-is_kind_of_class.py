#!/usr/bin/python3
"""
Checks if the object is an instance of the class,
or an instance of a class that inherited from the specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if obj is an instance of a_class or
    a class that a_class inherits from.
    Args:
        obj: The object to check.
        a_class: The class to check against.
    Returns:
        True if obj is an instance or
        inherits from a_class, otherwise False.
    """
    return isinstance(obj, a_class)
