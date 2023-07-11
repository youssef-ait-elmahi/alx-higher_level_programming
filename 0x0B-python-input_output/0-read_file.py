#!/usr/bin/python3
""" Module reads from a file """


def read_file(filename=""):
    """ Function reads file
    Args:
        filename: filename
    Raises
        Exception: can file be opened
    """
    with open(filename, 'r', encoding="utf-8") as f:
        r = f.read()
        print(r, end='')
