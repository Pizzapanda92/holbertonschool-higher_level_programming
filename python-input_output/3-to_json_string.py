#!/usr/bin/python3
"""
function that returns the JSON representation of an object (string)
"""
import json


def to_json_string(my_obj):
    """
    Write the Python object directly to the file in JSON format
    """
    return json.dumps(my_obj)
