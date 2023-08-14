#!/usr/bin/python3

def max_integer(my_list=[]):
    list_len = len(my_list)
    next_num = my_list[0]

    if list_len == 0:
        return None

    for i in range(list_len):
        if my_list[i] > next_num:
            next_num = my_list[i]
        return next_num
