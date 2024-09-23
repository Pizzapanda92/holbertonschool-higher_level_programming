#!/usr/bin/python3
"""A class BaseGeometry with an unimplemented area method"""


class BaseGeometry:
    """Represents a geometry object"""

    def area(self):
        """Raises an Exception to indicate that the method is not implemented"""
        raise Exception("area() is not implemented")
