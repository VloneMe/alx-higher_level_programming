#!/usr/bin/python3
'''
Module for the Base class
'''

import json
import os
import csv
import turtle


class Base:
    '''
    This base class representing the foundation for other classes.
    '''

    __nb_objects = 0

    def __init__(self, id=None):
        '''
        This initializes an instance of the Base class.

        Args:
            id (int): The id of the object (optional).
        '''

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''
        This converts a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): List of dictionaries.

        Returns:
            str: The JSON representation of the list of dictionaries.
        '''

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        This saves a list of objects to a JSON file.

        Args:
            list_objs (list): List of objects to save.
        '''

        if list_objs is None:
            list_objs = []
        full_list_json = [obj.to_dictionary() for obj in list_objs]
        empty_list_json = cls.to_json_string(full_list_json)
        with open(cls.__name__ + '.json', 'w') as f:
            f.write(empty_list_json)

    @staticmethod
    def from_json_string(json_string):
        '''
        This converts a JSON string to a list of dictionaries.

        Args:
            json_string (str): The JSON string to convert.

        Returns:
            list: List of dictionaries.
        '''

        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''
        This creates an instance of the class with
        attributes set from a dictionary.

        Args:
            dictionary (dict): Dictionary containing the attribute values.

        Returns:
            object: Instance of the class with attributes set.
        '''

        if cls.__name__ == 'Rectangle':
            instance_class = cls(10, 2, 3)
        elif cls.__name__ == 'Square':
            instance_class = cls(10)
        else:
            instance_class = cls()

        instance_class.update(**dictionary)
        return instance_class

    @classmethod
    def load_from_file(cls):
        '''
        This loads a list of objects from a JSON file.

        Returns:
            list: List of instances created from the JSON file.
        '''

        file_path = cls.__name__ + '.json'
        if not os.path.isfile(file_path):
            return []

        with open(file_path) as f:
            to_json = f.read()
        dict_list = Base.from_json_string(to_json)
        obj_list = [cls.create(**obj_dict) for obj_dict in dict_list]
        return obj_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''
        This saves a list of objects to a CSV file.

        Args:
            list_objs (list): List of objects to save.
        '''

        if cls.__name__ == 'Rectangle':
            file_name = 'Rectangle.csv'
            headers = ['id', 'width', 'height', 'x', 'y']
        elif cls.__name__ == 'Square':
            file_name = 'Square.csv'
            headers = ['id', 'size', 'x', 'y']
        else:
            return

        with open(file_name, 'w') as fil:
            csv_writer = csv.DictWriter(fil, fieldnames=headers)
            csv_writer.writeheader()
            for obj in list_objs:
                dict_row = obj.to_dictionary()
                csv_writer.writerow(dict_row)

    @classmethod
    def load_from_file_csv(cls):
        '''
        This loads a list of objects from a CSV file.

        Returns:
            list: List of instances created from the CSV file.
        '''

        if cls.__name__ == 'Rectangle':
            file_name = 'Rectangle.csv'
        elif cls.__name__ == 'Square':
            file_name = 'Square.csv'
        else:
            return []

        list_csv = []
        with open(file_name) as f:
            dict_reader = csv.DictReader(f)
            for row in dict_reader:
                dict_row = {key: int(value) for key, value in row.items()}
                list_csv.append(cls.create(**dict_row))
        return list_csv

    @staticmethod
    def draw(list_rectangles, list_squares):
        '''
        This opens a window and draws all the rectangles and squares.

        Args:
            list_rectangles (list): List of Rectangle instances.
            list_squares (list): List of Square instances.
        '''

        screen = turtle.Screen()
        screen.bgcolor("orange")
        screen.title("Task21")
        t = turtle.Turtle()

        for rectangle in list_rectangles:
            t.up()
            t.goto(rectangle.x, rectangle.y)
            t.color("Royal Blue")
            t.down()
            for _ in range(2):
                t.forward(rectangle.width)
                t.left(90)
                t.forward(rectangle.height)
                t.left(90)

        for square in list_squares:
            t.up()
            t.goto(square.x, square.y)
            t.color("Red")
            t.down()
            for _ in range(4):
                t.forward(square.width)
                t.left(90)

        turtle.done()
