#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
a = 10
b = 5
result = add(a, b)
print(f"{a} + {b} = " + "{}".format(result))

result1 = sub(a, b)

print(f"{a} - {b} = " + "{}".format(result1))

result2 = mul(a, b)

print(f"{a} * {b} = " + "{}".format(result2))

result2 = div(a, b)
print(f"{a} / {b} = " + "{}".format(result2))
