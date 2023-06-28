#!/usr/bin/python3
# Coordinates of a square
"""
This class defines a class Square.
"""


class Square:
    """
    This class reepresent a square.

    Attributes:
        size (int): The size of the square.
        position (tuple): The position of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.

        Args:
            size (int, optional): The size of the new square.
            position (tuple, optional): The position of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        This gets or set the current size of the square.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        This sets the size of the square.

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

    @property
    def position(self):
        """
        This gets or sets the current position of the square.

        Returns:
            tuple: The current position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """This set the position of the square.

        Args:
            value (tuple): The position value to set.

        Raises:
            TypeError: If value is not a tuple or has incorrect length or contains non-integer elements.
            ValueError: If any element of the tuple is less than 0.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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

        Prints a square using the size and position attributes.
        If size is 0, an empty line is printed.
        """
        if self.__size == 0:
            print("")
            return

        [print("") for _ in range(self.__position[1])]
        for _ in range(self.__size):
            [print(" ", end="") for _ in range(self.__position[0])]
            [print("#", end="") for _ in range(self.__size)]
            print("")
