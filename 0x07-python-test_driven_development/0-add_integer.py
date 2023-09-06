#!/usr/bin/python3

"""add function"""


def add_integer(a, b=98):
    """This is an addition python function
    Args:
        a: first integer argument
        b: second integer argument
    Raise:
        TypeError
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a+b)
