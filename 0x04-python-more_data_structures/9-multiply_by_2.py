#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    newd = a_dictionary.copy()
    for key, value in newd.items():
        newd[key] = value * 2
    return newd
