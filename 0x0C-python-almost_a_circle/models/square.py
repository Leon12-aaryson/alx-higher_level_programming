#!/usr/bin/python3
"""
this module is for the square class
it inherits the rectangle class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    this is the square class created
    it inherits from the Rectangle class from
    rectangle module
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        instantiation function/method
        """
        super().__init__(size, x, y, id)

    def __str__(self):
        """string representation of a Square"""
        return (f"[Square] ({self.id}) "
                f"{self.x}/{self.y} - "
                f"{self.width}"
                )

    @property
    def size(self):
        """fetches the size of Square"""
        return self.width

    @size.setter
    def size(self, value):
        """assigns value to width and height"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value
            self.height = value

    def update(self, *args, **kwargs):
        """assigns arguments to attributes"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size" or key == "width" or key == "height":
                    self.width = value
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        returns the dictionary representation
        of the squar
        """
        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y,
                }
