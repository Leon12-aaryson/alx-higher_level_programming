#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):

    num1 = 0

    for num2 in range(0, x):
        try:
            print("{:d}".format(my_list[num2]), end="")
            num1 += 1
        except (ValueError, TypeError):  # IndexError?
            continue
    print()
    return (num1)
