#!/usr/bin/python3

import dis
if __name__ == "__main__":
    def magic_calculation_102(a, b):
        from magic_calculation_102 import add, sub

        if a < b:
            add = magic_calculation_102.add
            c = add(a, b)

            for i in range(4, 6):
                c = add(c, i)

        else:
            sub = magic_calculation_102.sub
            return sub(a, b)
        return c

dis.dis(magic_calculation_102)
