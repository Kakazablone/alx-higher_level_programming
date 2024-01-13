#!/usr/bin/python3
""" My Module for converting objects into representation for JSON"""


def class_to_json(obj):
    """ Turns an object into nice representation for JSON
    Args:
        obj (object): object to transform"""
    return obj.__dict__
