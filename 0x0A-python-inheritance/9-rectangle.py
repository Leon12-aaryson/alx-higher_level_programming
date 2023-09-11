#!/usr/bin/python3
"""
creation of new module rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class Rectangle
    Args:
        BaseGeometry
    """
    def __init__(self, width, height):
        """
        innitalizaion of module method
        constructor creted
        Args:
            width
            height
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        area method
        """
        return self.__width * self.__height

    def __str__(self):
        """
        str magic method
        """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
