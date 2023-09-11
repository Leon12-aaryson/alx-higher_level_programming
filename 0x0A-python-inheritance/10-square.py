#!/usr/bin/python3
"""
Module for square created
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class creation
    """
    def __init__(self, size):
        """
        method initialization of class
        constructor method
        Args:
            size
        """
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        area method
        """
        return super().area()
