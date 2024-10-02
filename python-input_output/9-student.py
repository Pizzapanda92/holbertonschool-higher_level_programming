#!/usr/bin/python3
"""
class Student that defines a student
"""


def __init__(self, first_name, last_name, age):
    """
        Initialize the student with first name, last name, and age.
    """
    self.first_name = first_name
    self.last_name = last_name
    self.age = age


def to_json(self):
    """
        Return a dictionary representation of the instance.
    """
    return self.__dict__
