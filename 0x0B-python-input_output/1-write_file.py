#!/usr/bin/python3
"""write file function"""


def write_file(filename="", text=""):
    """ String Write

    Args:
        text (str): string
    Return:
        written number of characters.
    """

    with open(filename, "w", encoding='utf-8') as mideh:
        return mideh.write(text)
