#!/usr/bin/python3
"""
Class Rectangle that defines a rectangle by its width and height.
"""


class Rectangle:
    """
    Represents a rectangle with private
    instance attributes 'width' and 'height'.
    Provides getter and setter for 'width' and 'height' with validation.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle with a given width and height.

        Args:
            width (int): The width of the rectangle, default is 0.
            height (int): The height of the rectangle, default is 0.
        """

        self.height = height
        self.width = width

    @property
    def width(self):
        """
        Getter method for width.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for width. Validates the value before setting it.

        Args:
            value (int): The new width of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for height.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for height. Validates the value before setting it.

        Args:
            value (int): The new height of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value