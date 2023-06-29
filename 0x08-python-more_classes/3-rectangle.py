#!/usr/bin/python3
""" more on rectangle """
class Rectangle:
    def __init__(self, width=0, height=0):
        """this func acting as a constructor """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.

        Args:
            value (int): The width value to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """

        if isinstance(value, int):
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """Get the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.

        Args:
            value (int): The height value to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if isinstance(value, int):
            if value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value
        else:
            raise TypeError("height must be an integer")

    def area(self):
        """ return the area"""
        return self.__width*self.__height

    def perimeter(self):
        """ returns the perimeter """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2*self.__width + 2*self.__height

    def __str__(self):
        """  string presentation """
        if self.__width == 0 or self.__height == 0:
            return ""
        fill_hash = ""
        
        for i in range(self.__height):
            for j in range(self.__width):
                fill_hash += "#" 
                
            fill_hash += "\n"
    
        return fill_hash[:-1]
