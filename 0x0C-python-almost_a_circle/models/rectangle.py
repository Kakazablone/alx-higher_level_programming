#!/usr/bin/python3
"""Rectangle Module"""
from models.base import Base


class Rectangle(Base):
    """Rectangle inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Attribute initialization
        Args:
            width (int): reps width of the rectangle
            height (int): reps height of the rectangle
            x (int): offset to shift the rectangle when printing
            y (int): offset to shift the rectangle when printing
            id (int): count of instances of rectangles"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """Informal string representation of the Rectangle"""

        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """ Updates attributes of the Rectangle
        Args:
            args (non-keyword arguments): non-specified amount of arguments
            kwargs (key-word arguments): non-specified amount of arguments
        """

        attrs = ["id", "width", "height", "x", "y"]

        for position, value in enumerate(args):
            if position > (len(attrs) - 1):
                break
            setattr(self, attrs[position], value)

        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def area(self):
        """ Returns the area of the rectangle"""

        return self.width * self.height

    def display(self):
        """Uses #'s to print the rectangle"""

        print("\n"*self.y, end="")
        for row2 in range(self.height):
            print(" "*self.x + "#"*self.width)

    def to_dictionary(self):
        """ Returns the dictionary representation of the instance"""
        new_dict = {}
        attrs = ["id", "width", "height", "x", "y"]

        for att in attrs:
            new_dict[att] = getattr(self, att)

        return new_dict

    @staticmethod
    def validate_integer(var_name, value):
        """validation of all setter methods
        Args:
            var_name (str): the variable name
            value (int): the value associated with var_name"""

        error_1 = ["width", "height"]
        error_2 = ["x", "y"]

        if type(value) != int:
            raise TypeError("{} must be an integer".format(var_name))
        if var_name in error_1 and value <= 0:
            raise ValueError("{} must be > 0".format(var_name))
        if var_name in error_2 and value < 0:
            raise ValueError("{} must be >= 0".format(var_name))

    @property
    def width(self):
        """ Get width"""

        return self.__width

    @width.setter
    def width(self, value):
        """ Set width
        Args:
            value (int): the value to set to width"""

        self.validate_integer("width", value)
        self.__width = value

    @property
    def height(self):
        """ Get height"""

        return self.__height

    @height.setter
    def height(self, value):
        """ Set for height
        Args:
            value (int): the value to set to height"""

        self.validate_integer("height", value)
        self.__height = value

    @property
    def x(self):
        """ Get x"""

        return self.__x

    @x.setter
    def x(self, value):
        """ Set x
        Args:
            value (int): the value to assign to x"""

        self.validate_integer("x", value)
        self.__x = value

    @property
    def y(self):
        """ Get y"""

        return self.__y

    @y.setter
    def y(self, value):
        """ Set y
        Args:
            value (int): the value to assign to y"""

        self.validate_integer("y", value)
        self.__y = value
