#!/usr/bin/python3
""" My Module for creating a Student class"""


class Student():
    """ Creates a student"""

    def __init__(self, first_name, last_name, age):
        """ Initializes a student
        Args:
            first_name (str): Student's first name
            last_name (str): Student's last name
            age (int): age of Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Returns dictionary description of the instance"""
        my_dict = {}
        new_dict = self.__dict__
        if attrs is None:
            return new_dict
        for key, value in new_dict.items():
            if key in attrs:
                my_dict[key] = value
        return my_dict
