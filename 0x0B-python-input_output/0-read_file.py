#!/usr/bin/python3

""" lets start with files """

def read_file(filename=""):
    """
    Reads a text file and prints its contents to stdout.

    Args:
        filename (str): The name of the file to be read. (default: "")

    Returns:
        None

    Raises:
        FileNotFoundError: If the specified file does not exist.
        IOError: If there is an error while reading the file.

    Usage:
        read_file("filename.txt")  # Reads the contents of "filename.txt" and prints them to stdout.
        read_file()  # Reads the contents of a file specified by the user and prints them to stdout.

    """
    with open(filename, encoding='utf-8') as read_file:
        content = read_file.read()
        print(content, end="")

