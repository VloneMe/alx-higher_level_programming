#!/usr/bin/python3
# 9. Compare 2 squares
"""
This class defines a class Square.
"""



class Square:
    """
    This class represents a square.
    """

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the square. Default is 0.
        """
        self._size = 0  # Private instance attribute

        self.size = size  # Call the setter for validation

    @property
    def size(self):
        """Get the size of the square.

        Returns:
            int or float: The size of the square.
        """
        return self._size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int or float): The size of the square.

        Raises:
            TypeError: If the size is not a number (int or float).
            ValueError: If the size is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def area(self):
        """Calculate the area of the square.

        Returns:
            float: The area of the square.
        """
        return self._size ** 2

    def __eq__(self, other):
        """Compare two squares for equality.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the squares are equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() == other.area()
        return NotImplemented

    def __ne__(self, other):
        """Compare two squares for inequality.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the squares are not equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() != other.area()
        return NotImplemented

    def __lt__(self, other):
        """
        This compare if a square is less than another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True / False otherwise.
        """
        if isinstance(other, Square):
            return self.area() < other.area()
        return NotImplemented

    def __le__(self, other):
        """
        This compare if a square is less than or equal to another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True /  False otherwise.
        """
        if isinstance(other, Square):
            return self.area() <= other.area()
        return NotImplemented

    def __gt__(self, other):
        """
        This compare if a square is greater than another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True / False otherwise.
        """
        if isinstance(other, Square):
            return self.area() > other.area()
        return NotImplemented

    def __ge__(self, other):
        """
        This compare if a square is greater than or equal to another square.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True / False.
        """
        if isinstance(other, Square):
            return self.area() >= other.area()
        return NotImplemented

