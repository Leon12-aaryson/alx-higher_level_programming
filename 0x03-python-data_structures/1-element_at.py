#!/usr/bin/python3
def element_at(my_list, idx):
    listlen = len(my_list) - 1
    if idx < 0:
        return None
    elif idx > listlen:
        return None
    else:
        for i in my_list:
            return my_list[idx]
