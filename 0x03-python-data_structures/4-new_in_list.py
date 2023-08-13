#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list = my_list.copy()
    print(f"copy of list {list}")
    if (idx < 0) or (idx > (len(my_list) - 1)):
        return my_list
    else:
        list[idx] = element
    return list
