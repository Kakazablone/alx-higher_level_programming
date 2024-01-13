#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests the function max_integer for correct output
    """

    def test_max_at_the_end(self):
        """Tests all positive numbers
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_one_negative_number(self):
        """Test when there is a negative number in the list
        """
        self.assertEqual(max_integer([1, 2, -1, 3, 4]), 4)

    def test_only_negatives(self):
        """Tests a list of only negative numbers in the list
        """
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)

    def test_zero(self):
        """Tests a list size of 0
        """
        self.assertEqual(max_integer([]), None)

    def test_positive_and_negative(self):
        """Test a list with positive and negative numbers
        """
        self.assertEqual(max_integer([1, 6, 100, 4, 0, -1, 10]), 100)

    def test_max_in_the_middle(self):
        """Test when max is in the middle
        """
        self.assertEqual(max_integer([2, 3, 6, 4, 5]), 6)

    def test_max_at_the_beginning(self):
        """Test with max at the beginning of list
        """
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_list_with_one_element(self):
        """Test with a list that only has 1 element
        """
        self.assertEqual(max_integer([1]), 1)


if __name__ == '__main__':
    unittest.main()
