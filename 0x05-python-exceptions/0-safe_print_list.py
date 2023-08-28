#!/bin/python3
def safe_print_list(my_list=[], x=0):
    lenlist1 = 0
    for lenlist in range(x):
        try:
            print(my_list[lenlist], end="")
            lenlist1 += 1
        except IndexError:
            break

    print()
    return (lenlist1)
