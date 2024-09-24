#!/usr/bin/python3
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """
    Abstract class that defines a blueprint for shapes.
    Requires any subclass to implement the 'area' and 'perimeter' methods.
    """

    @abstractmethod
    def area(self):
        """
        Abstract method to calculate the area of the shape.
        Must be implemented by any subclass.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract method to calculate the perimeter of the shape.
        Must be implemented by any subclass.
        """
        pass


class Circle(Shape):
    """
    Concrete class representing a circle.
    Inherits from Shape and implements the area and perimeter methods.
    """

    def __init__(self, radius):
        """
        Initializes a Circle with a given radius.
        """
        self.radius = radius

    def area(self):
        """
        Calculates and returns the area of the circle.
        Formula: pi * radius^2
        """
        return pi * self.radius ** 2

    def perimeter(self):
        """
        Calculates and returns the perimeter (circumference) of the circle.
        Formula: 2 * pi * radius
        """
        return 2 * pi * self.radius


class Rectangle(Shape):
    """
    Concrete class representing a rectangle.
    Inherits from Shape and implements the area and perimeter methods.
    """

    def __init__(self, largeur, longeur):
        """
        Initializes a Rectangle with a given width (largeur)
        and length (longeur).
        """
        self.largeur = largeur
        self.longeur = longeur

    def area(self):
        """
        Calculates and returns the area of the rectangle.
        Formula: length * width
        """
        return self.longeur * self.largeur

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.
        Formula: 2 * (length + width)
        """
        return 2 * (self.longeur + self.largeur)


def shape_info(shape):
    """
    Prints the area and perimeter of a given shape.
    This function uses duck typing to assume that the passed object has
    'area' and 'perimeter' methods.
    """
    area = shape.area()
    perimeter = shape.perimeter()

    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")
