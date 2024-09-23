#!/usr/bin/python3
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
