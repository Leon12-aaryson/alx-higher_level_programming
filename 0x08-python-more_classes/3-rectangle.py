#!/usr/bin/python3
"""Definition of the rectangle class"""


class Rectangle:
    """Rectangle class represenation."""

    def __init__(self, width=0, height=0):
        """instantiation of the rectangle
        Args:
        width (int): width.
        height (int): height.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """obtaining the Rectangle width."""
        return self.__width

    @width.setter
    def width(self, value):
        """errors """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """obtaining the Rectangle height."""
        return self.__height

    @height.setter
    def height(self, value):
        """ error checking and reporting """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the Rectangle area."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the Rectangle perimeter."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Returns a triangle Representaion."""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rectangle = []
        for i in range(self.__height):
            [rectangle.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rectangle.append("\n")
        return ("".join(rectangle))
