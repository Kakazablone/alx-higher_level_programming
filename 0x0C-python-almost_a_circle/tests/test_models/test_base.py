#!/usr/bin/python3
"""Module for testing the Base class"""
import unittest
import io
import sys
import os
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Performs tests on the Base class"""

    def test_empty_arg(self):
        """When no arguments are passed"""

        Base._Base__nb_objects = 0
        b = Base()
        self.assertEqual(b.id, 1)

    def test_with_arg(self):
        """Test that id is being assigned correctly"""

        Base._Base__nb_objects = 0
        b = Base(50)
        self.assertEqual(b.id, 50)

    def test_multiple_instances(self):
        """Test if id is correct after multiple instances"""

        Base._Base__nb_objects = 0
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base()

        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 4)

    def test_reassign_id(self):
        """ Test if id is correct in all instances after reassigning it"""

        Base._Base__nb_objects = 0
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base()

        instances = [b1, b2, b3, b4]
        position = 0

        for i in range(100, 500, 100):
            instances[position].id = i
            self.assertEqual(instances[position].id, i)
            position += 1

    def test_to_json_string(self):
        """ Test if the to_json_string method works"""

        json_string = Base.to_json_string([{'x': 5}])
        json_string_two = Base.to_json_string([{'x': 5}, {'y': 3}])

        self.assertEqual(json_string, '[{"x": 5}]')
        self.assertEqual(json_string_two, '[{"x": 5}, {"y": 3}]')

    def test_to_json_string_none(self):
        """ Test what happens when to_json_string is passed None"""

        json_string = Base.to_json_string(None)

        self.assertEqual(json_string, '[]')

    def test_to_json_string_empty_list(self):
        """ Test what happens when to_json_string is passed an empty list"""

        json_string = Base.to_json_string([])

        self.assertEqual(json_string, '[]')

    def test_save_to_file_one(self):
        """ Test if save_to_file method works"""

        r1 = Rectangle(10, 7, 2, 8, 50)
        s1 = Square(8, 2, 3, 60)
        r1_dictionary = [{"y": 8, "x": 2, "id": 50, "width": 10, "height": 7}]
        s1_dictionary = [{"id": 60, "y": 3, "x": 2, "size": 8}]

        Rectangle.save_to_file([r1])
        Square.save_to_file([s1])

        with open("Rectangle.json", "r") as file1:
            r1_file_dict = file1.read()

        with open("Square.json", "r") as file2:
            s1_file_dict = file2.read()

        r1_file_dict = json.loads(r1_file_dict)
        s1_file_dict = json.loads(s1_file_dict)

        self.assertEqual(r1_file_dict, r1_dictionary)
        self.assertEqual(s1_file_dict, s1_dictionary)

        os.remove("./Rectangle.json")
        os.remove("./Square.json")

    def test_save_to_file_two(self):
        """ Test if save_to_file method can handle empty lists"""

        r1_dictionary = []
        s1_dictionary = []

        Rectangle.save_to_file([])
        Square.save_to_file([])

        with open("Rectangle.json", "r") as file1:
            r1_file_dict = file1.read()

        with open("Square.json", "r") as file2:
            s1_file_dict = file2.read()

        r1_file_dict = json.loads(r1_file_dict)
        s1_file_dict = json.loads(s1_file_dict)

        self.assertEqual(r1_file_dict, r1_dictionary)
        self.assertEqual(s1_file_dict, s1_dictionary)

        os.remove("./Rectangle.json")
        os.remove("./Square.json")

    def test_save_to_file_three(self):
        """Test if save_to_file method can handle None"""

        r1_dictionary = []
        s1_dictionary = []

        Rectangle.save_to_file(None)
        Square.save_to_file(None)

        with open("Rectangle.json", "r") as file1:
            r1_file_dict = file1.read()

        with open("Square.json", "r") as file2:
            s1_file_dict = file2.read()

        r1_file_dict = json.loads(r1_file_dict)
        s1_file_dict = json.loads(s1_file_dict)

        self.assertEqual(r1_file_dict, r1_dictionary)
        self.assertEqual(s1_file_dict, s1_dictionary)

        os.remove("./Rectangle.json")
        os.remove("./Square.json")

    def test_from_json_string_one(self):
        """ Test if from_json_string method works on Rectangle"""

        list_input = [{'id': 89, 'width': 10, 'height': 4},
                      {'id': 7, 'width': 1, 'height': 7}]

        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)

        expected = [{"height": 4, "width": 10, "id": 89},
                    {"height": 7, "width": 1, "id": 7}]

        self.assertEqual(list_output, expected)

    def test_from_json_string_two(self):
        """ Test if from_json_string method works on Square"""

        list_input = [{'id': 89, 'size': 10},
                      {'id': 7, 'size': 1}]

        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)

        expected = [{'id': 89, 'size': 10},
                    {'id': 7, 'size': 1}]

        self.assertEqual(list_output, expected)

    def test_from_json_string_three(self):
        """ Test when from_json_string receives None"""

        list_input = None

        json_list_output = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_output)

        expected = []

        self.assertEqual(list_output, expected)

    def test_from_json_string_four(self):
        """ Test when from_json_string receives empty list"""

        list_input = []
        json_list_output = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_output)

        expected = []

        self.assertEqual(list_output, expected)

    def test_create_one(self):
        """ Test if the create method works"""

        capturedOutput1 = io.StringIO()
        sys.stdout = capturedOutput1

        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        expected = "[Rectangle] (1) 1/0 - 3/5\n"

        print(r1)

        capturedOutput2 = io.StringIO()
        sys.stdout = capturedOutput2

        print(r2)

        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)
        self.assertEqual(capturedOutput1.getvalue(), expected)
        self.assertEqual(capturedOutput2.getvalue(), expected)

        sys.stdout = sys.__stdout__

    def test_load_from_file_one(self):
        """ Test if load_from_file works with Rectangle"""

        Base._Base__nb_objects = 0

        capturedOutput1 = io.StringIO()
        sys.stdout = capturedOutput1

        r1 = Rectangle(10, 7, 2, 8)
        list_rectangles_input = [r1]

        Rectangle.save_to_file(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file()

        for rect in list_rectangles_output:
            print(rect)

        expected = "[Rectangle] (1) 2/8 - 10/7\n"

        self.assertEqual(capturedOutput1.getvalue(), expected)

        os.remove("./Rectangle.json")
        sys.stdout = sys.__stdout__

    def test_load_from_file_two(self):
        """ Test when load_from_file accessing a file that doesn't exist"""

        Base._Base__nb_objects = 0

        capturedOutput1 = io.StringIO()
        sys.stdout = capturedOutput1

        r1 = Rectangle(10, 7, 2, 8)
        list_rectangles_input = [r1]

        list_rectangles_output = Rectangle.load_from_file()

        print(list_rectangles_output)

        self.assertEqual(capturedOutput1.getvalue(), "[]\n")

        sys.stdout = sys.__stdout__

    def test_load_from_file_three(self):
        """Test if load_from_file works with Square"""

        Base._Base__nb_objects = 0

        capturedOutput1 = io.StringIO()
        sys.stdout = capturedOutput1

        s1 = Square(10, 7, 8)
        list_squares_input = [s1]

        Square.save_to_file(list_squares_input)

        list_squares_output = Square.load_from_file()

        for sq in list_squares_output:
            print(sq)

        self.assertEqual(capturedOutput1.getvalue(), "[Square] (1) 7/8 - 10\n")

        os.remove("./Square.json")
        sys.stdout = sys.__stdout__
