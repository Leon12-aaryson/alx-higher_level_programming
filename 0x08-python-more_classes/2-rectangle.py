#!/usr/bin/python3
"""
creation of the rectangle class
"""


class Rectangle:
    """ Rectangle class"""
    def __init__(self, width=0, height=0):
        """innitialize the class object
        Args:
            height: height argument
            width: width argument
        Raises:
            TypeError: When value is not of required type
            ValueError: when value is inappropriate
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """retrieves width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setting the height of rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """create the area object"""
        return (self.__width * self.__height)

    def perimeter(self):
        """create the perimeter object"""
        if (self.__height == 0) or (self.___width == 0):
            return (0)
        return ((self.__height * 2) + (self.__width * 2))
