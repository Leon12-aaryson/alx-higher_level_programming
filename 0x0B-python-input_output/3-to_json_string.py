#!/usr/bin/python3
"""
file I/O module
"""
import json


def to_json_string(my_obj):
    """
    returns json rep of a string
    """
    return json.dumps(my_obj)
