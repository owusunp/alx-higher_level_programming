#!/usr/bin/python3
""" more on rectangle """
class Rectangle:
    def __init__(self, width=0, height=0):
        """this func acting as a constructor """
        self.__width = width
        self.__height = height

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

    def area(self):
        """ return the area"""
        return self.__width*self.__height

    def perimeter(self):
        """ returns the perimeter """
        
        return 2*self.__width + 2*self.__height

    def __str__(self):
        """  string presentation """
        if self.__width == 0 or self.height == 0:
            return 0
        for i in range(self.__height - 1):
            for j in range(self.__width):
                print("{:s}".format("#"), end="")
            print()
        for i in range(1):
            for j in range(self.__width):
                print("{:s}".format("#"), end="")
        return str("")
