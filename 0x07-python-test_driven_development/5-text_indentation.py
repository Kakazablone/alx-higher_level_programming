#!/usr/bin/python3
"""My string module performs operations on strings
"""


def text_indentation(text):
    """Prints 2 new lines after each . ? or : character in a string

    Args:
        text (str): The text to perform operation on
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    operators = ['.', '?', ':']
    new_str = ""
    for letter in text:
        new_str += letter
        if letter in operators:
            new_str += "\n"
            print(new_str.strip(" "))
            new_str = ""
    if letter not in operators:
        print(new_str.strip(" "), end="")
