#!/usr/bin/python3
def no_c(my_string):
    cpy = [i for i in my_string if i != 'C' and i != 'c']
    return ("".join(cpy))
