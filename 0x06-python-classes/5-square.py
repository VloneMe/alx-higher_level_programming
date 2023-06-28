#!/usr/bin/python3
# 5. Printing a square
"""
This class define a class Square.
"""


class Square:
    """
    This represent a square.

    Attributes:
        size (int): The size of the square.
    """

    def __init__(self, size):
        """
        This initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """
        This gets or sets the size of the square.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        this set the size of the square.

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
        """
        This calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        This print the square using the # character.

        Prints a square using the size attribute.
        If size is 0, an empty line is printed.
        """
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
