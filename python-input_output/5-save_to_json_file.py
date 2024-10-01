#!/usr/bin/python3
""" function that returns an object (Python data structure)
represented by a JSON string"""

import json


def save_to_json_file(my_obj, filename):
    """
    Write the Python object directly to the file in JSON format
    """
    return json.dump(my_obj, filename)
