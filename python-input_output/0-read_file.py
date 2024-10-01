#!/usr/bin/python3
"""
Function that reads a UTF-8 encoded text file and prints its content to stdout.
"""


def read_file(filename=""):
    """"
    Args:
        filename (str): The name of the file to be read. Default is an empty string.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
