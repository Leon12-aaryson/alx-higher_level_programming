#!/usr/bin/python3
"""
Module docs
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class docs
    """
    def __init__(self, width, height):
        """
        INNITIALIZE AN OBJECT
        Use of constructor
        Args:
            width: first object
            heght: heght of rectangle
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
