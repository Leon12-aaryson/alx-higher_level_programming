#!/usr/bin/python3
"""
creatio of python classes
"""


class MyInt(int):
    """
    Class MyInt creation
    """

    def __eq__(self, other):
        """
        allows equality operator behaviour in a function
        """
        return self.real != other

    def __ne__(self, other):
        """
        Non equal function or magic method
        """
        return self.real == other
