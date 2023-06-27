#!/usr/bin/python3

"""Square Class Definition"""


class Square:
    """Innitialisation"""

    def __init__(self, size=0):
        """
        Arg:
            size: A integer representing object size with default value of 0.
        Raises:
            TypeError: if size is not an integer.
            ValueError: If size < 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
