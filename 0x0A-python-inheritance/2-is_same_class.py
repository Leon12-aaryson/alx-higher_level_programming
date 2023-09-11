#!/usr/bin/python3
"""
module created for checking if attributes are of
same method
"""


def is_same_class(obj, a_class):
    """
    method is_same_class created
    attrib:
        obj (obj): object 1
        a_class (obj): object 2

    Returns:
        bool: if same True else False
    """

    return type(obj) is a_class
