#!/usr/bin/python3

class Square:
    '''Creation of the class Square'''

    def __init__(self, size=0):
        '''instatmtiating the class'''
        self.__size = size

        if isinstance(size, int):
            try:
                return None
            except TypeError:
                print("size must be an integer")
        elif size < 0:
            try:
                return size
            except ValueError:
                print("size must be >= 0")
