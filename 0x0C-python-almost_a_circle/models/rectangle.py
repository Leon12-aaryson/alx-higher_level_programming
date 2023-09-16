#!/usr/bin/python3
"""
this is a module for creation of the rectangle
class
"""
from models.base import Base


class Rectangle(Base):
    """
    creating the rectangle class.
    Rectangle class inherits from base class in base module
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        instantiation of a class rectangle
        Args:
            width: rectangle width
            height: rectangle height
            x: first rectangle coordinate
            y: second rectangle coordinate
        Raise:
            No errors raised yet
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
