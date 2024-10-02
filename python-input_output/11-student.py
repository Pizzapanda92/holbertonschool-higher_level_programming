#!/usr/bin/python3
"""
    A class that defines a student by their first name, last name, and age.
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """
        Initialize the student with first name, last name, and age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
    Retrieves a dictionary representation of a Student instance.
    If attrs is a list of strings, only those attributes are retrieved.
    Otherwise, all attributes are retrieved.
    """
        if isinstance(attrs, list):
            result = {}
            for attr in attrs:
                if attr in self.__dict__:
                    result[attr] = self.__dict__[attr]
            return result

        else:
            return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance based on the JSON dictionary.
        """
        for key in json:
            if key in self.__dict__:
                self.__dict__[key] = json[key]
