#!/usr/bin/python3
"""Defining an object attribute lookup function"""


def lookup(obj):
    """Return a list of public attributes and methods of an object."""
    return (dir(obj))
