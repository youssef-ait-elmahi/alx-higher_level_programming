#!/usr/bin/python3
""" Module returns the JSON of an object"""
import json


def to_json_string(my_obj):
    """ Function returns JSON of an object
    Args:
        my_obj: object
    Raises:
        Exception: when the object can't be encoded
    """
    return json.dumps(my_obj)
