#!/usr/bin/python3
def print_revered_list_integer(my_list=[]):
    if isinstance(my_list, list):
        my_list.reverse()
        for i in my_list:
            print("{}".format(i))
