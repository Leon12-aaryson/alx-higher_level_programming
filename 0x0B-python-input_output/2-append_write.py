#!/usr/bin/python3
"""Append_write """


def append_write(filename="", text=""):
    """ To appends a file

    Args: text (str): a string.
    Return: Number of characters added.
    """

    with open(filename, "a", encoding='utf-8') as mideh:
        return mideh.write(text)
