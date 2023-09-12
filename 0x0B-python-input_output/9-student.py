#!/usr/bin/python3
"""
module with student class
"""


class Student:
    """
    class student created
    """
    def __init__(self, first_name, last_name, age):
        """
        innitiate xlass constrctor
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        function to json
        """
        return self.__dict__
