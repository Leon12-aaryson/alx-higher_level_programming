#!/usr/bin/python3

def uniq_add(my_list=[]):
    set1 = set(my_list)
    sum = 0
    for number in set1:
        sum += number
    return sum
