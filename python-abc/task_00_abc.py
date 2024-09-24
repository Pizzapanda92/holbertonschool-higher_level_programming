#!/usr/bin/python3
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract class Animal defines a contract for subclasses to implement.
    Inherits from ABC (Abstract Base Class) to declare an abstract class.
    """
    @abstractmethod
    def sound(self):
        """
        Abstract method 'sound' must be implemented by all subclasses of Animal.
        This method has no body here, it only defines the contract.
        """
        pass


class Dog(Animal):
    """
    Dog class inherits from the abstract class Animal.
    It is required to implement the abstract 'sound' method.
    """

    def sound(self):
        """
        Implements the 'sound' method, returning 'Bark' as the sound of a dog.
        """
        return ('Bark')


class Cat(Animal):
    """
    Cat class also inherits from the abstract class Animal.
    It is required to implement the 'sound' method as well.
    """

    def sound(self):
        """
        Implements the 'sound' method, returning 'Meow' as the sound of a cat.
        """
        return ('Meow')
