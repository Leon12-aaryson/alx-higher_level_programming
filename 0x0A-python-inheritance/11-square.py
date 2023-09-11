#!/usr/bin/python3
"""
Module square created
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class created
    Args:
        Rectangle
    """
    def __init__(self, size):
        """
        class innitialization also as 
        constructor
        Args:
            size: is size of square
        """
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        area method
        """
        return super().area()

    def __str__(self):
        """
        str magic class
        """
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
