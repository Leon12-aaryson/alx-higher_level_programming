#!/usr/bin/python3
"""Rectangle class Definition in the python code"""


class Rectangle:
    """Rectangle class Representtion.
    Attributes:
    number_of_instances (int): The number of Rectangle instances.
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Innitialisation of the new reactangle instance
        Args:
        width (int): rectangle width.
        height (int): rectangle height.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """obtain the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """obtain the Rectangle height."""
        return self.__height

    @height.setter
    def height(self, value):
        """ Errror checking occurs and reports on errors"""
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
        """Returns printable rectangle """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rectangle = []
        for i in range(self.__height):
            [rectangle.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rectangle.append("\n")
        return ("".join(rectangle))

    def __repr__(self):
        """Returns the Rectangle string."""
        rectangle = "Rectangle(" + str(self.__width)
        rectangle += ", " + str(self.__height) + ")"
        return (rectangle)

    def __del__(self):
        """Prints on deletion."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
