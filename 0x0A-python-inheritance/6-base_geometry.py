#!/usr/bin/python3


""" this is the base geometry """
class BaseGeometry:
    """
    Base class for geometry objects.

    Methods:
        area(): Raises an exception indicating that area calculation is not implemented.

    """
    def area(self):
        """
        Calculate the area of the geometry object.

        Raises:
            Exception: Indicates that the area calculation is not implemented.

        """
        raise Exception("area() is not implemented")

