#!/usr/bin/python3


"""LETS DEFINE THIS FUNC"""
def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of, or if it is an instance of a class that inherited from, the specified class.

    Args:
        obj: The object to be checked.
        a_class: The specified class to compare against.

    Returns:
        True if the object is an instance of the specified class or any of its subclasses, False otherwise.
    """
    return isinstance(obj, a_class)

