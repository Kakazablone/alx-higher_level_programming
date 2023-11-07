#!/usr/bin/python3
""" My Module for reading a file"""


def read_file(filename=""):
    """ Reads the file, filename, and prints to standard out
    Args:
        filename (str): The file to read"""
    with open(filename, encoding="UTF-8") as f:
        print(f.read(), end="")
