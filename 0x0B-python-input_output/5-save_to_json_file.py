#!/usr/bin/python3
"""
Json module in file I/O
"""
import json


def save_to_json_file(my_obj, filename):
    """
    write to an object file with json
    """
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
