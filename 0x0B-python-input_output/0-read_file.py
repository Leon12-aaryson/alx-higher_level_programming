#!/usr/bin/python3
"""
this is a module for file I/O
"""


def read_file(filename=""):
    """
    methd to read file using with
    Args:
        filename: this stands for path or name of file
    """
    with open(filename, "r", encoding="UTF-8") as read_file:
        file_details =  read_file.read()
        print(file_details)
