#!/usr/bin/python3
"""defines a locked class"""


class LockedClass:
    """creation of LockedClass
    The class prevents users from dynamically creating
    new instance attributes except for the specified first_name attrib

    Attributes:
        first_name
    """

    __slots__ = ['first_name']
