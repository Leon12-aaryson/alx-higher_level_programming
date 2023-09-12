#!/usr/bin/python3
"""
module for writong into files
"""


def write_file(filename="", text=""):
    """
    creation of method to write into files
    """
    with open(filename, 'w', encoding="utf-8") as f:
        numc = f.write(text)
    return numc
