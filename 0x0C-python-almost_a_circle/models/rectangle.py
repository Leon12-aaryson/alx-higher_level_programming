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
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        width property
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        width method instantiated
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        creation of the height property
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height setter
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        creation of x property
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        x setter created
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        creation of y property
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        setter for value of y
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        public method to return area of a rectangle
        """
        return (self.__width * self.__height)

    def display(self):
        """
        creation of the display method that
        outputs # while looping height and width
        """
        for _ in range(self.height):
            print("#" * self.width)

    def __str__(self):
        """
        overiding the rectangle method using __str__
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
