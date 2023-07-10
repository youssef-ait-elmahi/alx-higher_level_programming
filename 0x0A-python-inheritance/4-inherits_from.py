#!/usr/bin/python3
"""
module sub class
"""


def inherits_from(obj, a_class):
    """returns True if the object is an instance of a class
       otherwise False.
    """
    if type(obj) != a_class:
        return issubclass(type(obj), a_class)
    else:
        return False
