#!/usr/bin/python3
def magic_calculation_102(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
        c = add(a, b)

        for i in range(4, 6):
            c = add(c, i)
    else:
        return sub(a, b)
    return c


import dis
dis.dis(magic_calculation_102)
