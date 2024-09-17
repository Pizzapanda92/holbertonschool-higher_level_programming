#!/usr/bin/python3
"""
Module that defines a class Square.
"""


class Square:
    """
    Represents a square with private instance attributes 'size' and 'position'.
    Provides getter and setter for 'size' and 'position' with validation.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the square with a given size and position.

        Args:
            size (int): The size of the square's side, default is 0.
            position (tuple): The position offset of the square, default is (0, 0).
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Getter method for position.

        Returns:
            tuple: The position of the square as a tuple of 2 positive integers.
        """

        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for position. Validates the value before setting it.

        Args:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """

        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(num, int) for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
            # Print the vertical offset (empty lines)
            for _ in range(self.position[1]):
                print("")
            # Print each line of the square with horizontal offset
            for i in range(self.size):
                print(" " * self.position[0] + "#" * self.size)
