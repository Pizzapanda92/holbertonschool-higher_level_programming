#!/usr/bin/python3
"""
Module that defines a class Square.
"""


class Square:
    """
    Represents a square with a private instance attribute 'size'.
    Provides getter and setter for 'size' with validation.
    """

    def __init__(self, size=0):
        """
        Initializes the square with a given size.

        Args:
            size (int): The size of the square's side, default is 0.
        """

        self.size = size

    @property
    def size(self):
        """
        Getter method for size.

        Returns:
            int: The size of the square's side.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for size. Validates the value before setting it.

        Args:
            value (int): The new size of the square's side.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """

        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square using the character '#'.

        If size is 0, prints an empty line.
        """
        if self.size == 0:
            print("")
        else:
            for i in range(self.__size):
                print("#" * self.__size)
