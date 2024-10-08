#!/usr/bin/python3
"""A class BaseGeometry with an unimplemented area method"""


class BaseGeometry:
    """Represents a geometry object"""

    def area(self):
        """
        Raises an exception to indicate the method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates 'value' as an integer greater than 0.

        Raises:
        TypeError: If 'value' is not an integer.
        ValueError: If 'value' is <= 0.
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
