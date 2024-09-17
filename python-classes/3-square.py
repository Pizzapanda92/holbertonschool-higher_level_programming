#!/usr/bin/python3
"""
Module that defines a class Square.
"""


class Square:
    """
    Represents a square with a private instance attribute 'size'.
    """

    def __init__(self, size=0):
        """
        Initializes the square with a given size.

        Args:
            size (int): The size of the square's side, default is 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """

        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """

        return self.__size ** 2
