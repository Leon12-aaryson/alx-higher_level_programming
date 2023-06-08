#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add
    a = 10
    b = 5
    result = add(a, b)
    print(f"{a} + {b} = " + "{}".format(result))

    from calculator_1 import sub
    a = 10
    b = 5
    result1 = sub(a, b)
    print(f"{a} - {b} = " + "{}".format(result1))
    
    from calculator_1 import mul
    a = 10
    b = 5
    result2 = mul(a, b)
    print(f"{a} * {b} = " + "{}".format(result2))

    from calculator_1 import div
    a = 10
    b = 5
    result2 = div(a, b)
    print(f"{a} / {b} = " + "{}".format(result2))
