#!/usr/bin/python3
import pickle



class CustomObject:
    """
    A class representing a custom object with attributes name, age, and is_student.
    This class includes methods for displaying the object's attributes and for serializing
    and deserializing the object using the pickle module.
    """
    def __init__(self, name, age, is_student):
        """
        Initialize the object with name, age, and student status.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the object's attributes.
        """
        print("Name: {}\nAge: {}\nIs Student: {}".format(
            self.name, self.age, self.is_student))

    def serialize(self, filename):
        """
        Save the object to a file using pickle.
        """
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        """
        Load an object from a file using pickle.
        """
        with open(filename, 'rb') as file:
            return pickle.load(file)
