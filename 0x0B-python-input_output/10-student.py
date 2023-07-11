#!/usr/bin/python3
"""
 Student to JSON with filter
"""


class Student:
    """
    A class Student that defines a student by: (based on 9-student.py)
    """

    def __init__(self, first_name, last_name, age):
        """
        This initialize a new Student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        This retrieve a dictionary representation of a student instance.

        Args:
            attrs (list, optional): List of attributes
            to include in the dictionary.
                Defaults to None.

        Returns:
            dict: A dictionary representation of the student.
        """

        if attrs is None:
            return self.__dict__

        result = {}
        for attr in attrs:
            if attr in self.__dict__:
                result[attr] = self.__dict__[attr]
        return result
