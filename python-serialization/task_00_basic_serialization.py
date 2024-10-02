#!/usr/bin/python3
import json


def serialize_and_save_to_file(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)
    pass


def load_and_deserialize(filename):
    with open(filename, 'r') as json_file:
        return json.load(json_file)
    pass
