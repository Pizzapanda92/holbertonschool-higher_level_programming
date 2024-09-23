#!/usr/bin/python3
"""
A subclass of list that includes a method
to print the list in sorted order.
"""


class MyList(list):
    """
    Class that inherits from list and
    adds a print_sorted method
    """

    def print_sorted(self):
        """
        Prints the list sorted in ascending order
        without modifying the original list
        """
        print(sorted(self))
