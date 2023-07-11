#!/usr/bin/python3
""" Module creates an Object from JSON"""
import json


def load_from_json_file(filename):
    """ Function creates Object from JSON
    Args:
        filename: textfile name
    Raises:
        Exception: when the object can't be encoded
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
