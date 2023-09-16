#!/usr/bin/python3
"""
This is the initial files or module for the project
for creating the base class
"""


class Base:
    """
    creation of the base class in the base module
    creation of the __nb_objects attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
