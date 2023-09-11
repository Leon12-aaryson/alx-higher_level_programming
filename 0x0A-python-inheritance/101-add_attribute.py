#!/usr/bin/python3
"""
creation of methods
"""


def add_attribute(a_class, att_name, att_value):
    """
    add_attribute method
    Attrib:
        a_class: first attrib
        att_name: second attribute for attribute name
        att__value: is for attribute value
    Raises:
        TypeError: Raise when not of required type
    """
    if not hasattr(a_class, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(a_class, att_name, att_value)
