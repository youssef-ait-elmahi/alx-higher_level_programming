#!/usr/bin/python3
""" Module Object to a text file using JSON"""
import json


def save_to_json_file(my_obj, filename):
    """ Function object to a text file with JSON
    Args:
        my_obj: object
        filename: textfile name
    Raises:
        Exception: when the object can't be encoded
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
