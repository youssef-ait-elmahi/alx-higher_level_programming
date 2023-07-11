#!/usr/bin/python3
""" Module returns an object by as JSON"""
import json


def from_json_string(my_str):
    """ Function returns an object as JSON
    Args:
        my_str: JSON representation
    Raises:
        Exception: string can't be decoded
    """
    return json.loads(my_str)
