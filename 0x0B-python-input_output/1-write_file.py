#!/usr/bin/python3

""" THUS COME STRESS ME """

def write_file(filename="", text=""):
    """
    Writes the specified text to a file.

    Args:
        filename (str): The name of the file to be written. (default: "")
        text (str): The text to be written to the file. (default: "")

    Returns:
        int: The number of characters written to the file.

    Raises:
        IOError: If there is an error while writing to the file.

    Usage:
        write_file("filename.txt", "Hello, World!")  # Writes "Hello, World!" to "filename.txt" and returns the number of characters written.
        write_file()  # Writes the user-specified text to a file and returns the number of characters written.

    """
    with open(filename, mode="w", encoding="utf-8") as read_char:
        return read_char.write(text)

