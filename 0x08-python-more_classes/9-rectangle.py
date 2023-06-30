#!/usr/bin/python3

""" this id the final project on recttangle class"""


class Rectangle:
    """ lets do come coding down here in the class """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ acting as like a constructor"""
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1
    
    @property
    def width(self):
        """ returns the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ it sets the width """
        if isinstance(value, int):
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """ returns the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ it sets the height """
        if isinstance(value, int):
            if value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value
        else:
            raise TypeError("height must be an integer")    

    def area(self):
        """ return the area of a rectangle """
        return self.__width*self.__height

    def perimeter(self):
        """ returns the perimeter of a rectangle """

        if self.__height == 0 or self.__width == 0:
            return 0
        return 2*(self.__width + self.__height)
    
    def __str__(self):
        """ give the string representation """
        if self.__height == 0 or self.__width == 0:
            return ""

        accept_all = ""
        for i in range(self.__width):
            for j in range(self.__height):
                accept_all += str(self.print_symbol)
            accept_all += "\n"

        return accept_all[:-1]

    def __repr__(self):
        """ returns the human readable string representation """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """ message printed when an instance is deleted """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
    
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ returns the bigger rectangle """
        if isinstance(rect_1, Rectangle):
            pass
        else:
            raise TypeError("rect_1 must be an instance of Rectangle")

        if isinstance(rect_2, Rectangle):
            pass
        else:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """ returns a new Rectangle instance with width == height == size """
        return cls(size, size)

