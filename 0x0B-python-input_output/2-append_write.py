#!/usr/bin/python3
"""
file I/o in python
"""


def append_write(filename="", text=""):
    """
    python method to write and append data into file
    """
    with open(filename, "a", encoding="utf-8") as f:
        num = f.write(text)
    return num
