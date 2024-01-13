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

    def to_json(self):
        """ Returns dictionary description of the instance"""
        return self.__dict__
