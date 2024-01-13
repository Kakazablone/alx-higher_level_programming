#!/usr/bin/python3
"""Module for creating a base class"""
import json
import csv
import turtle


class Base:
    """To be used as a base for all other classes

    Attributes:
        __nb_objects (private): represents the number of objects"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Assigns the public instance attribute with arg value if not None,
            otherwise assign the number of objects (after incrementing) to
            public instance attribute id

        Args:
            id (int)"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts the dictionary representation of an instance into JSON
        Args:
            list_dictionaries (list): list of an instances"""

        if list_dictionaries is None or len(list_dictionaries) == 0:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """ Returns the Python version of a JSON string"""

        if json_string is None or len(json_string) == 0:
            json_string = "[]"

        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Loads a list of objects, turns those objects into a list of
            dictionaries then sends them to a function that turns them into
            a JSON string, then saves it to a file, based on the name of a
            class."""

        filename = "{}.json".format(cls.__name__)
        obj_list = []

        if list_objs is not None:
            for obj in list_objs:
                obj_list += [obj.to_dictionary()]

        json_list = Base.to_json_string(obj_list)

        with open(filename, "w+", encoding="UTF-8") as f:
            f.write(json_list)

    @classmethod
    def create(cls, **dictionary):
        """ Creates a new instance of Square or Rectangle based off
    dictionary"""

        if "size" in dictionary:
            dummy = cls(1)
        else:
            dummy = cls(1, 1)

        dummy.update(**dictionary)

        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""

        from_filename = "{}.json".format(cls.__name__)
        instance_list = []

        try:
            with open(from_filename, mode="r+", encoding="UTF-8") as f:
                raw_json = f.read()
            list_of_dicts = cls.from_json_string(raw_json)
            for d in list_of_dicts:
                instance_list += [cls.create(**d)]
        except FileNotFoundError:
            pass
        return instance_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes in CSV
        Args:
           list_objs(list): List of objects"""
        filename = "{}.csv".format(cls.__name__)
        data = []
        if list_objs is not None:
            for obj in list_objs:
                dictionary = obj.to_dictionary()
                data.append(dictionary)
        rectangle_header = ['id', 'width', 'height', 'x', 'y']
        square_header = ['id', 'size', 'x', 'y']
        with open(filename, mode='w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                if cls.__name__ == 'Rectangle':
                    result = csv.DictWriter(f, fieldnames=rectangle_header)
                elif cls.__name__ == 'Square':
                    result = csv.DictWriter(f, fieldnames=square_header)
                result.writeheader()
                result.writerows(data)

    @classmethod
    def load_from_file_csv(cls):
        """Method that deserializes in CSV"""
        filename = "{}.csv".format(cls.__name__)
        instance_list = []
        try:
            with open(filename) as f:
                result = csv.DictReader(f)
                for row in result:
                    row = dict(row)
                    for key in row:
                        row[key] = int(row[key])
                    instance = cls.create(**row)
                    instance_list.append(instance)
        except FileNotFoundError:
            return instance_list
        return instance_list

@staticmethod
def draw_shapes(rectangles, squares):
    def draw_rectangle(t, x, y, width, height):
        t.pencolor("blue")
        t.fillcolor("white")
        t.pensize(5)
        t.speed(1)

        t.penup()
        t.goto(x, y)
        t.pendown()

        for _ in range(2):
            t.forward(width)
            t.left(90)
            t.forward(height)
            t.left(90)

        t.penup()

    def draw_square(t, x, y, size):
        t.pencolor("red")
        t.fillcolor("white")
        t.pensize(5)
        t.speed(0.5)

        t.penup()
        t.goto(x, y)
        t.pendown()

        for _ in range(4):
            t.forward(size)
            t.left(90)

        t.penup()

    screen = turtle.Screen()
    screen.title("My first draw with Python and turtle module")
    screen.bgcolor("black")

    turtle_pen = turtle.Turtle()
    turtle_pen.shape("turtle")

    for rectangle in rectangles:
        draw_rectangle(turtle_pen, *rectangle)

    for square in squares:
        draw_square(turtle_pen, *square)

    turtle.done()
