#!/usr/bin/python3
"""
creation of list module with list class
"""


class MyList(list):
    """
    class MyList created
    ATTRIB:
        list: first attribute
    """

    def print_sorted(self):
        """
        method to print sorted list
        """
        sorted_list = super().copy()
        sorted_list.sort()
        print(sorted_list)
