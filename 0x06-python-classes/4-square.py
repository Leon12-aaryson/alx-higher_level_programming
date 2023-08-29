#!/usr/bin/python3

'''Defining a Square class'''


class Square:
    '''A class defining a square'''

    def __init__(self, size=0):
        '''Instantiating an object of the square class
        Args:
            size: first parameter
        '''
        self.size = size

    @property
    def size(self):
        '''Getter method for attribute size'''
        return (self.__size)

    @size.setter
    def size(self, value):
        '''Setter method for attribute size'''
        if ((type(value) == str) or (type(value) == float)):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        '''Method that calculates the area of a square'''
        return (self.__size * self.__size)
