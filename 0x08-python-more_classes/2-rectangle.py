#!/usr/bin/python3
"""Definition of the class"""


class Rectangle:
    """Rectangle class representation."""

    def __init__(self, width=0, height=0):
        """instantition of the class
        Args:
        width (int): The width of the new rectangle.
        height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """obtaining the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """error checking and reporting """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """obtaining the rectangle height."""
        return self.__height

    @height.setter
    def height(self, value):
        """ error checking occurs for errors"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
