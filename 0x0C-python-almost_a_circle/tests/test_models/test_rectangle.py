"""Module for testing the Rectangle class"""
import unittest
import io
import sys
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Runs tests on the rectangle class"""

    def test_negative_width(self):
        """Test when width is negative"""

        with self.assertRaises(ValueError) as err:
            r1 = Rectangle(-5, 4, 3, 2)
        self.assertEqual(str(err.exception), "width must be > 0")

    def test_zero_width(self):
        """ Test when width is zero"""

        with self.assertRaises(ValueError) as err:
            r1 = Rectangle(0, 50, 2, 3)
        self.assertEqual(str(err.exception), "width must be > 0")

    def test_negative_height(self):
        """ Test when height is negative"""

        with self.assertRaises(ValueError) as err:
            r1 = Rectangle(2, -5, 4, 3)
        self.assertEqual(str(err.exception), "height must be > 0")

    def test_zero_height(self):
        """ Test when height is zero"""

        with self.assertRaises(ValueError) as err:
            r1 = Rectangle(2, 0, 3, 4)
        self.assertEqual(str(err.exception), "height must be > 0")

    def test_negative_x(self):
        """ Test when x is negative"""

        with self.assertRaises(ValueError) as err:
            r1 = Rectangle(1, 2, -3, 4)
        self.assertEqual(str(err.exception), "x must be >= 0")

    def test_negative_y(self):
        """ Test when y is negative"""

        with self.assertRaises(ValueError) as err:
            r1 = Rectangle(1, 2, 3, -4)
        self.assertEqual(str(err.exception), "y must be >= 0")

    def test_all_arguments(self):
        """ Test with all argument fields passed"""

        r1 = Rectangle(1, 2, 3, 4, 5)

        self.assertEqual(r1.id, 5)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)

    def test_list_width(self):
        """ Test when width is passed a list"""

        with self.assertRaises(TypeError) as err:
            r1 = Rectangle([5], 4, 3, 2, 1)
        self.assertEqual(str(err.exception), "width must be an integer")

    def test_dict_width(self):
        """ Test when width is passed a dict"""

        with self.assertRaises(TypeError) as err:
            r1 = Rectangle({"width": 5}, 4, 3, 2, 1)
        self.assertEqual(str(err.exception), "width must be an integer")

    def test_float_width(self):
        """ Test when width is passed a float"""

        with self.assertRaises(TypeError) as err:
            r1 = Rectangle(5.5, 4, 3, 2, 1)
        self.assertEqual(str(err.exception), "width must be an integer")

    def test_tuple_width(self):
        """ Test when width is passed a tuple"""

        with self.assertRaises(TypeError) as err:
            r1 = Rectangle((3, 4), 4, 3, 2, 1)
        self.assertEqual(str(err.exception), "width must be an integer")

    def test_string_width(self):
        """ Test when width is passed a string"""

        with self.assertRaises(TypeError) as err:
            r1 = Rectangle("Penguin", 4, 3, 2, 1)
        self.assertEqual(str(err.exception), "width must be an integer")

    def test_list_height(self):
        """ Test when height is passed a list"""

        with self.assertRaises(TypeError) as err:
            r1 = Rectangle(5, [4], 3, 2, 1)
        self.assertEqual(str(err.exception), "height must be an integer")

    def test_dict_height(self):
        """ Test when height is passed a dict"""

        with self.assertRaises(TypeError) as err:
            r1 = Rectangle(4, {"height": 5}, 3, 2, 1)
        self.assertEqual(str(err.exception), "height must be an integer")

    def test_float_height(self):
        """ Test when height is passed a float"""

        with self.assertRaises(TypeError) as err:
            r1 = Rectangle(5, 4.5, 3, 2, 1)
        self.assertEqual(str(err.exception), "height must be an integer")

    def test_tuple_height(self):
        """ Test when height is passed a tuple"""

        with self.assertRaises(TypeError) as err:
            r1 = Rectangle(3, (4, 5), 3, 2, 1)
        self.assertEqual(str(err.exception), "height must be an integer")

    def test_string_height(self):
        """ Test when height is passed a string"""

        with self.assertRaises(TypeError) as err:
            r1 = Rectangle(4, "Penguin", 3, 2, 1)
        self.assertEqual(str(err.exception), "height must be an integer")

    def test_list_x(self):
        """ Test when x is passed a list"""

        with self.assertRaises(TypeError) as err:
            r1 = Rectangle(5, 4, [3], 2, 1)
        self.assertEqual(str(err.exception), "x must be an integer")

    def test_dict_x(self):
        """ Test when x is passed a dict"""

        with self.assertRaises(TypeError) as err:
            r1 = Rectangle(4, 3, {"x": 5}, 2, 1)
        self.assertEqual(str(err.exception), "x must be an integer")

    def test_float_x(self):
        """ Test when x is passed a float"""

        with self.assertRaises(TypeError) as err:
            r1 = Rectangle(5, 4, 3.5, 2, 1)
        self.assertEqual(str(err.exception), "x must be an integer")

    def test_tuple_x(self):
        """ Test when x is passed a tuple"""

        with self.assertRaises(TypeError) as err:
            r1 = Rectangle(3, 4, (3, 2), 2, 1)
        self.assertEqual(str(err.exception), "x must be an integer")

    def test_string_x(self):
        """ Test when x is passed a string"""

        with self.assertRaises(TypeError) as err:
            r1 = Rectangle(4, 3, "Penguin", 2, 1)
        self.assertEqual(str(err.exception), "x must be an integer")

    def test_list_y(self):
        """ Test when y is passed a list"""

        with self.assertRaises(TypeError) as err:
            r1 = Rectangle(5, 4, 3, [2], 1)
        self.assertEqual(str(err.exception), "y must be an integer")

    def test_dict_y(self):
        """ Test when y is passed a dict"""

        with self.assertRaises(TypeError) as err:
            r1 = Rectangle(4, 3, 2, {"y": 5}, 1)
        self.assertEqual(str(err.exception), "y must be an integer")

    def test_float_y(self):
        """ Test when y is passed a float"""

        with self.assertRaises(TypeError) as err:
            r1 = Rectangle(5, 4, 3, 2.5, 1)
        self.assertEqual(str(err.exception), "y must be an integer")

    def test_tuple_y(self):
        """ Test when y is passed a tuple"""

        with self.assertRaises(TypeError) as err:
            r1 = Rectangle(3, 4, 3, (1, 2), 1)
        self.assertEqual(str(err.exception), "y must be an integer")

    def test_string_y(self):
        """ Test when y is passed a string"""

        with self.assertRaises(TypeError) as err:
            r1 = Rectangle(4, 3, 2, "Penguin", 1)
        self.assertEqual(str(err.exception), "y must be an integer")

    def test_area(self):
        """ Test for correct output for area"""

        r1 = Rectangle(3, 3, 0, 0, 10)
        r2 = Rectangle(4, 4)
        r3 = Rectangle(2, 2, 3)
        r4 = Rectangle(2, 1, 4, 3)

        self.assertEqual(r1.area(), 9)
        self.assertEqual(r2.area(), 16)
        self.assertEqual(r3.area(), 4)
        self.assertEqual(r4.area(), 2)

    def test_display_number_zero(self):
        """ Test if display of rectangle is correct"""

        display = "##\n##\n##\n"
        capturedOutput = io.StringIO()  # Create StringIO Object
        sys.stdout = capturedOutput  # Redirect stdout

        r1 = Rectangle(2, 3)

        r1.display()  # Call Function
        self.assertEqual(capturedOutput.getvalue(), display)  # use .getvalue

        sys.stdout = sys.__stdout__  # Reset redirect

    def test_dunder_str(self):
        """ Test if __str__ is returning the correct string"""

        mssg = "[Rectangle] (20) 1/0 - 3/4\n"

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        r1 = Rectangle(3, 4, 1, 0, 20)
        print(r1)

        self.assertEqual(capturedOutput.getvalue(), mssg)

        sys.stdout = sys.__stdout__

    def test_id(self):
        """ Tests the id of the rectangle"""

        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 2)
        r2 = Rectangle(1, 1)
        r3 = Rectangle(10, 2, 0, 0, 12)

        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)

    def test_width(self):
        """ Test correct width being set"""

        r1 = Rectangle(10, 2)
        r2 = Rectangle(666, 333)

        self.assertEqual(r1.width, 10)
        self.assertEqual(r2.width, 666)

    def test_height(self):
        """ Test correct height being set"""

        r1 = Rectangle(10, 2)
        r2 = Rectangle(30, 50)

        self.assertEqual(r1.height, 2)
        self.assertEqual(r2.height, 50)

    def test_no_arguments(self):
        """ Test when width and height aren't passed"""

        with self.assertRaises(TypeError):
            r1 = Rectangle()

    def test_with_one_argument(self):
        """ Test when only width is passed"""

        with self.assertRaises(TypeError):
            r1 = Rectangle(1)

    def test_with_width_and_height(self):
        """ Test when width and height are passed"""

        Base._Base__nb_objects = 0

        r1 = Rectangle(3, 4)
        r2 = Rectangle(10, 20)

        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 3)
        self.assertEqual(r1.height, 4)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.width, 10)
        self.assertEqual(r2.height, 20)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)

    def test_with_x_passed(self):
        """ Test when width, height, and x are passed"""

        Base._Base__nb_objects = 0

        r1 = Rectangle(4, 3, 1)
        r2 = Rectangle(20, 10, 4)

        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 0)

        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.width, 20)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.x, 4)
        self.assertEqual(r2.y, 0)

    def test_with_up_to_y_passed(self):
        """ Test when width, height, x, and y are passed"""

        Base._Base__nb_objects = 0

        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(4, 3, 2, 1)

        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)

        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.width, 4)
        self.assertEqual(r2.height, 3)
        self.assertEqual(r2.x, 2)
        self.assertEqual(r2.y, 1)

    def test_update_with_one_argument(self):
        """ Test the update method with 1 argumen"""

        r1 = Rectangle(10, 10, 10, 10, 10)

        self.assertEqual(r1.id, 10)

        r1.update(89)

        self.assertEqual(r1.id, 89)

    def test_update_with_two_arguments(self):
        """ Test the update method with 2 arguments"""

        r1 = Rectangle(10, 10, 10, 10, 10)

        self.assertEqual(r1.id, 10)
        self.assertEqual(r1.width, 10)

        r1.update(89, 2)

        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)

    def test_update_with_three_arguments(self):
        """ Test the update method with 3 arguments"""

        r1 = Rectangle(10, 10, 10, 10, 10)

        self.assertEqual(r1.id, 10)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 10)

        r1.update(89, 2, 3)

        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)

    def test_update_with_four_arguments(self):
        """ Test the update method with 4 arguments"""

        r1 = Rectangle(10, 10, 10, 10, 10)

        self.assertEqual(r1.id, 10)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r1.x, 10)

        r1.update(89, 2, 3, 4)

        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)

    def test_update_with_five_arguments(self):
        """ Test the update method with 5 arguments"""

        r1 = Rectangle(10, 10, 10, 10, 10)

        self.assertEqual(r1.id, 10)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r1.x, 10)
        self.assertEqual(r1.y, 10)

        r1.update(89, 2, 3, 4, 5)

        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)

    def test_update_with_kwargs_id(self):
        """ Test if only kwargs and id works"""

        r1 = Rectangle(10, 10, 10, 10, 10)

        r1.update(id=50)

        self.assertEqual(r1.id, 50)

    def test_update_with_kwargs_width(self):
        """ Test if only kwargs and width works"""

        r1 = Rectangle(10, 10, 10, 10, 10)

        r1.update(width=20)

        self.assertEqual(r1.width, 20)

    def test_update_with_kwargs_height(self):
        """ Test if only kwargs and height works"""

        r1 = Rectangle(10, 10, 10, 10, 10)

        r1.update(height=20)

        self.assertEqual(r1.height, 20)

    def test_update_with_kwargs_x(self):
        """ Test if only kwargs and x works"""

        r1 = Rectangle(10, 10, 10, 10, 10)

        r1.update(x=20)

        self.assertEqual(r1.x, 20)

    def test_update_with_kwargs_y(self):
        """ Test if only kwargs and y works"""

        r1 = Rectangle(10, 10, 10, 10, 10)

        r1.update(y=20)

        self.assertEqual(r1.y, 20)

    def test_update_with_two_kwargs(self):
        """ Test if 2 kwargs are passed"""

        r1 = Rectangle(10, 10, 10, 10, 10)

        r1.update(id=900, width=30)

        self.assertEqual(r1.id, 900)
        self.assertEqual(r1.width, 30)

    def test_update_with_three_kwargs(self):
        """ Test if 3 kwargs are passed"""

        r1 = Rectangle(10, 10, 10, 10, 10)

        r1.update(id=900, width=30, height=60)

        self.assertEqual(r1.id, 900)
        self.assertEqual(r1.width, 30)
        self.assertEqual(r1.height, 60)

    def test_update_with_two_kwargs(self):
        """ Test if 2 kwargs are passed"""

        r1 = Rectangle(10, 10, 10, 10, 10)

        r1.update(id=900, width=30, height=60, x=2)

        self.assertEqual(r1.id, 900)
        self.assertEqual(r1.width, 30)
        self.assertEqual(r1.height, 60)
        self.assertEqual(r1.x, 2)

    def test_update_with_two_kwargs(self):
        """ Test if 2 kwargs are passed"""

        r1 = Rectangle(10, 10, 10, 10, 10)

        r1.update(id=900, width=30, height=60, x=2, y=3)

        self.assertEqual(r1.id, 900)
        self.assertEqual(r1.width, 30)
        self.assertEqual(r1.height, 60)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 3)

    def test_update_with_one_args_and_kwargs(self):
        """ Test when args AND kwargs are passed"""

        r1 = Rectangle(10, 10, 10, 10, 10)

        r1.update(30, id=70)

        self.assertEqual(r1.id, 30)

    def test_with_two_args_and_kwargs(self):
        """ Test with multiple args and one kwarg"""

        r1 = Rectangle(10, 10, 10, 10, 10)

        r1.update(40, 20, id=80)

        self.assertEqual(r1.id, 40)
        self.assertEqual(r1.width, 20)

    def test_with_three_args_and_kwargs(self):
        """ Test with multiple args and one kwarg"""

        r1 = Rectangle(10, 10, 10, 10, 10)

        r1.update(40, 20, 55500, id=80)

        self.assertEqual(r1.id, 40)
        self.assertEqual(r1.width, 20)
        self.assertEqual(r1.height, 55500)

    def test_with_four_args_and_kwargs(self):
        """ Test with multiple args and one kwarg"""

        r1 = Rectangle(10, 10, 10, 10, 10)

        r1.update(40, 20, 55500, 2394, id=80)

        self.assertEqual(r1.id, 40)
        self.assertEqual(r1.width, 20)
        self.assertEqual(r1.height, 55500)
        self.assertEqual(r1.x, 2394)

    def test_with_five_args_and_kwargs(self):
        """ Test with multiple args and one kwarg"""

        r1 = Rectangle(10, 10, 10, 10, 10)

        r1.update(40, 20, 55500, 2394, 7789, id=80)

        self.assertEqual(r1.id, 40)
        self.assertEqual(r1.width, 20)
        self.assertEqual(r1.height, 55500)
        self.assertEqual(r1.x, 2394)
        self.assertEqual(r1.y, 7789)

    def test_full_args_and_kwargs(self):
        """ Test if all args and kwargs are passed"""

        r1 = Rectangle(10, 10, 10, 10, 10)

        r1.update(666, 555, 444, 333, 222,
                  id=66, width=55, height=44, x=33, y=22)

        self.assertEqual(r1.id, 666)
        self.assertEqual(r1.width, 555)
        self.assertEqual(r1.height, 444)
        self.assertEqual(r1.x, 333)
        self.assertEqual(r1.y, 222)

    def test_too_many_args(self):
        """ Test when a lot of args are passed"""

        r1 = Rectangle(10, 10, 10, 10, 10)

        r1.update(2, 2, 2, 2, 2, 666, 98, 23, 55, 900)

        self.assertEqual(r1.id, 2)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 2)

    def test_rectangle_to_dictionary(self):
        """ Test the to_dictionary method"""

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 2, 1, 9)

        expected_dict = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        r1_dictionary = r1.to_dictionary()

        print(type(r1_dictionary))

        self.assertEqual(r1_dictionary, expected_dict)
        self.assertEqual(capturedOutput.getvalue(), "<class 'dict'>\n")

        sys.stdout = sys.__stdout__

    def test_rectangle_to_dictionary_two(self):
        """ Test the to_dictionary method when only 2 var passed to rectangle
        """

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 8)

        expected_dict = {'x': 0, 'y': 0, 'id': 1, 'height': 8, 'width': 10}
        r1_dictionary = r1.to_dictionary()

        print(type(r1_dictionary))

        self.assertEqual(r1_dictionary, expected_dict)
        self.assertEqual(capturedOutput.getvalue(), "<class 'dict'>\n")

        sys.stdout = sys.__stdout__

    def test_rectangle_to_dictionary_three(self):
        """Test the to_dictionary method when only 3 var passed to rectangle"""

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 8, 3)

        expected_dict = {'x': 3, 'y': 0, 'id': 1, 'height': 8, 'width': 10}
        r1_dictionary = r1.to_dictionary()

        print(type(r1_dictionary))

        self.assertEqual(r1_dictionary, expected_dict)
        self.assertEqual(capturedOutput.getvalue(), "<class 'dict'>\n")

        sys.stdout = sys.__stdout__

    def test_rectangle_to_dictionary_four(self):
        """ Test the to_dictionary method when all var passed to rectangle"""

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 8, 3, 5, 30)

        expected_dict = {'x': 3, 'y': 5, 'id': 30, 'height': 8, 'width': 10}
        r1_dictionary = r1.to_dictionary()

        print(type(r1_dictionary))

        self.assertEqual(r1_dictionary, expected_dict)
        self.assertEqual(capturedOutput.getvalue(), "<class 'dict'>\n")

        sys.stdout = sys.__stdout__

    def test_rectangle_to_dictionary_five(self):
        """ Test the to_dictionary method when all var passed to rectangle
            and the Rectangle is update with the update method"""

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 8, 3, 5, 30)

        expected_dict = {'x': 3, 'y': 5, 'id': 30, 'height': 8, 'width': 10}
        r1_dictionary = r1.to_dictionary()

        print(type(r1_dictionary))

        self.assertEqual(r1_dictionary, expected_dict)
        self.assertEqual(capturedOutput.getvalue(), "<class 'dict'>\n")

        new_dict = {'x': 3, 'y': 5, 'id': 333, 'height': 8, 'width': 10}
        r1.update(id=333)

        r1_dict2 = r1.to_dictionary()

        self.assertEqual(r1_dict2, new_dict)

        sys.stdout = sys.__stdout__
