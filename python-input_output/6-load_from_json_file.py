#!/usr/bin/python3
"""Function that creates an object from a JSON file."""

import json


def load_from_json_file(filename):
    """
    Creates and returns an object from a JSON file.
    """

    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
