#!/usr/bin/python3
"""
Checks if the object is an instance of a class
that inherits (directly or indirectly) from the specified class,
but not an instance of the specified class itself.
"""


def inherits_from(obj, a_class):
    """
    Check if obj is an instance of a class that inherited from a_class,
    but not a direct instance of a_class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        True if obj is an instance of a subclass of a_class,
        otherwise False.
    """
    if type(obj) != a_class:
        return issubclass(type(obj), a_class)
    else:
        return False
