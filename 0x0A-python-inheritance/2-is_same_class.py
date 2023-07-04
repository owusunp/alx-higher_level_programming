#!/usr/bin/python3

"""LETS DEFINE THIS FUNCT"""

def is_same_class(obj, a_class):
    """
    Checks if the object is exactly an instance of the specified class.

    Args:
        obj: The object to be checked.
        a_class: The specified class to compare against.

    Returns:
        True if the object is exactly an instance of the specified class; False otherwise.

    """
    if isinstance(obj, a_class):
        return type(obj) is a_class
    return False

