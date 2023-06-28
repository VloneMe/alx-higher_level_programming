#!/usr/bin/python3
# 4. Access and update private attribute
"""
Define a class Square.
"""


class Square:
    """This class represent a square.

    Attributes:
        size (int): The size of the square.
    """

    def __init__(self, size=0):
        """This initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """This get or set the current size of the square.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ This sets the size of the square.

        Args:
            value (int): The size value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """This calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
