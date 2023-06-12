#!/usr/bin/python3


def max_integer(my_list=[]):
    list1 = len(my_list)
    bchar = my_list[0]

    if list1 == 0:
        return (None)

    for x in range(list1):
        if my_list[x] > big_char:
            bchar = my_list[x]

    return (bchar)
