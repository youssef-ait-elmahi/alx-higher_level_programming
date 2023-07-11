#!/usr/bin/python3
""" Module writes to a text file"""


def write_file(filename="", text=""):
    """ Function writes to file
    Args:
        filename: filename
        text: text to write
    Raises
        Exception: file can be opened
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
