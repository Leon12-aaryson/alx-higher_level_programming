#!/usr/bin/python3
"""class Student documentation """


class Student:
    """Class Student"""

    def __init__(self, first_name, last_name, age):
        """function for the class Student initialized

        Args:
            first_name (str): first name
            last_name (str): last name
            age (int): age
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns a dictionary representation of a Student.

        Args:
            attrs (python objects): objects to be retunerd

        """
        if not isinstance(attrs, list):
            return self.__dict__
        for attribute in attrs:
            if not isinstance(attribute, str):
                return self.__dict__
        new_dictionary = {}
        for str_att in attrs:
            if str_att in self.__dict__.keys():
                new_dictionary[str_att] = self.__dict__[str_att]
        return new_dictionary
