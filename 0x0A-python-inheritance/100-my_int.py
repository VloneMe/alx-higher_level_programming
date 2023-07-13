#!/usr/bin/python3
"""
My integer
"""


class MyInt(int):
    """
    A class that inherits from int.
    """

    def __init__(self, my_int):
        """
        Initializes the MyInt object with a value.

        Args:
            my_int (int): The integer value.

        Raises:
            TypeError: If my_int is not an integer.
        """
        if not isinstance(my_int, int):
            raise TypeError("my_int must be an integer")
        super().__init__(my_int)

    def __eq__(self, other):
        """
        Overrides the equality operator (==).

        Args:
            other (Any): The value to compare with.

        Returns:
            bool: True if the values are not equal, False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides the not equal operator (!=).

        Args:
            other (Any): The value to compare with.

        Returns:
            bool: True if the values are equal, False otherwise.
        """
        return super().__eq__(other)
