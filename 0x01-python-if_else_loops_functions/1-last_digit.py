#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)


def last1(number):
    last_no = abs(number) % 10
    return -last_no if (number < 0) else last_no


last = last1(number)

if last > 5:
    print(f"Last digit of {number} is {last} and is greater than 5")
elif last == 0:
    print(f"Last digit of {number} is {last} and is 0")
else:
    print(f"Last digit of {number} is {last} and is less than 6 and not 0")
