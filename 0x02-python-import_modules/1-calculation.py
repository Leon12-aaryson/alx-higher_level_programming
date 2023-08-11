#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, mul, div, sub

    a = 10
    b = 5

    add = add(a, b)
    print(f"{a} + {b} = {add}")

    sub = sub(a, b)
    print(f"{a} - {b} = {sub}")

    mul = mul(a, b)
    print(f"{a} * {b} = {mul}")
    
    #.format(a, b, mul))

    div = div(a, b)
    print("{} / {} = {}".format(a, b, div))
