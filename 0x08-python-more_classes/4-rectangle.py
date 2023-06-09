#!/usr/bin/python3
"""Rectangle class """


class Rectangle:
    """Rectangle r"""

    def __init__(self, width=0, height=0):
        """New Rectangle instantiation.
        Args:
        width (int): New rectangle width.
        height (int): New rectangle height.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """obtaining the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """ error checkoing and reporting """
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
        """ error checking"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns area."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns perimeter."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Returns Rectangle represenattion. """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rectangle = []
        for i in range(self.__height):
            [rectangle.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rectangle.append("\n")
        return ("".join(rectangle))

    def __repr__(self):
        """Returns the Rectangle string representation."""
        rectangle = "Rectangle(" + str(self.__width)
        rectangle += ", " + str(self.__height) + ")"
        return (rectangle)
