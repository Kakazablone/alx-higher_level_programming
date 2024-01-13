#!/usr/bin/python3
"""defines a square class"""


class Square:
    """Creates a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the size of a square
         Args:
            size (int): The size of the square
            position (tuple(int, int)):
                tuple 1: no. of spaces to print before the square
                tuple 2: no. of new lines to print before the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter - gets the size of the square
        Returns: The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter - sets the value of the size of the square
        Args:
            value (int): the size of the square
        """
        if type(value) != int:
            print("size must be an integer", end="")
            raise TypeError
        elif value < 0:
            print("size must be >= 0", end="")
            raise ValueError
        else:
            self.__size = value

    @property
    def position(self):
        """Getter - gets the position

        Returns: the value of the position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Setter - sets the value of the position
        Args:
            value (int): the position of the square
        """
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Calculates the area of the square
        Returns: The value of the area
        """
        return self.__size**2

    def my_print(self):
        """Prints out the square with #'s"""
        if self.__size != 0:
            for new_line in range(self.__position[1]):
                print()
            for index in range(self.__size):
                print(" "*self.__position[0], end="")
                print("#"*self.__size)
        else:
            print()
