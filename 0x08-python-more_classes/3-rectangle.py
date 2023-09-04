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
        if self.__height == 0 or self.__width == 0:
            return (0)
        return ((self.__height * 2) + (self.__width * 2))

    def __str__(self) -> str:
        """diagram printed by following the oject height and width"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle = ""
        for column in range(self.__height):
            for row in range(self.__width):
                rectangle += "#"
            if column < self.__height - 1:
                rectangle += "\n"
        return (rectangle)
