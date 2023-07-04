#!/usr/bin/python3
"""Prints the text with 2 new lines after each occurrence
of '.', '?', and ':' characters."""


def text_indentation(text):
    """
    Args:
        text (str): The input text.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    separators = ['.', '?', ':']
    result = ''
    i = 0

    while i < len(text):
        result += text[i]
        if text[i] in separators and i < len(text) - 1 and text[i + 1] == ' ':
            result += '\n\n'
            i += 2
        else:
            i += 1

    print(result.strip())
