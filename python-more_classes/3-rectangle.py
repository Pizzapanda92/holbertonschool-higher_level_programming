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

    def area(self):
        """
    Calculates and returns the area of the rectangle.

    The area is calculated by multiplying the width and height of the rectangle.

    Returns:
        int: The area of the rectangle.
    """

        return self.__height * self.__width

    def perimeter(self):
        """
    Calculates and returns the perimeter of the rectangle.

    The perimeter is calculated as twice the sum of the width and height.
    If either the width or height is zero, the perimeter is defined to be 0.

    Returns:
        int: The perimeter of the rectangle, or 0 if either the width or height is 0.
    """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        """
        print the rectangle with the character #
        """

        simbole = '#'
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.__height - 1):
            print(str(simbole) * self.__width)
        return (str(simbole) * self.__width)
