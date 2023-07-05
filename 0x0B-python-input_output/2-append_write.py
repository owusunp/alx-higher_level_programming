#!/usr/bin/python3

""" some append function """

def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file and returns the number of characters added.

    Args:
        filename (str): The name of the file to which the text will be appended. (default: "")
        text (str): The text to be appended to the file. (default: "")

    Returns:
        int: The number of characters added to the file.

    Usage:
        append_write("filename.txt", "This is the appended text.")  # Appends the specified text to "filename.txt" and returns the number of characters added.

    """
    with open(filename, mode='a', encoding='utf-8') as file:
        file.write(text)
        return len(text)

