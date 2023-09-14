#!/usr/bin/python3
"""
this is a module for file I/O
"""


def read_file(filename=""):
    """
    methd to read file using with
    Args:
        filename: this stands for path or name of file
    """
    with open(filename, "r", encoding="UTF-8") as read_file:
        file_details = read_file.read()
        print(file_details)
if __name__ == "__main__":
    file_path = "filename"
    read_file(file__path)
