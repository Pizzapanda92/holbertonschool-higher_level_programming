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

    """
    compteur of instances
    """
    number_of_instances = 0
    """
    gestion of symbol
    """
    print_symbol = '#'
    area = ""

    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle with a given width and height.

        Args:
            width (int): The width of the rectangle, default is 0.
            height (int): The height of the rectangle, default is 0.
        """

        self.height = height
        self.width = width
        """
        Increment the counter each time a new instance is created
        """
        Rectangle.number_of_instances += 1

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

    The area is calculated by multiplying the width and
    height of the rectangle.

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
        int: The perimeter of the rectangle, or 0 if either
        the width or height is 0.
    """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        """
        print the rectangle with the character #
        """

        self.print_symbol
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.__height - 1):
            print(str(self.print_symbol) * self.__width)
        return (str(self.print_symbol) * self.__width)

    def __repr__(self):
        """
    Provides a string representation of the Rectangle instance.

    The representation returned by this method is intended to be unambiguous
    and, ideally, should be a valid Python expression that could be used
    to recreate the object with the same values for width and height.

    Returns:
        str: A string representation of the Rectangle instance in the format
        'Rectangle(width, height)'.
    """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
    Prints a message when an instance of Rectangle is deleted.
    """
        print("Bye rectangle...")
        """
        Decrement the counter each time an instance is deleted
        """
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        """"
        compares area of rectangle 1 and 2
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        classmethod were width == height == size
        """

        return cls(size, size)
