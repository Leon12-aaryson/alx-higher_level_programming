#!/usr/bin/python3

'''Defining Square class'''


class Square:
    '''A class defining a square(Geometric shape)'''

    def __init__(self, size=0):
        '''Instantiating an square class
        Args:
            size: first parameter
        '''
        if ((type(size) == str) or (type(size) == float)):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        '''Method to calculates the area of a square'''
        return (self.__size * self.__size)
