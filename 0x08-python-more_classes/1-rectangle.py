#!/usr/bin/python3
""" more on rectangle """


class Rectangle:
    def __init__(self, width=0, height=0):
        """this func acting as a constructor """
        self.__width = width
        self.__height = height

    @property
    def height(self):
        """ returns height """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets the height """
        self.__height = value

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        else:
            if value < 0:
                raise ValueError("height must be >= 0")

    @property
    def width(self):
        """ returns width """
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width """
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        else:
            if value < 0:
                raise ValueError("width must be >= 0")

    



