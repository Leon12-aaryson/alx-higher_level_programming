#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
text = "Last digit of "
if last > 5:
    print(text + str(number) + " is " + str(last) + " and is greater than 5")
elif last == 0:
    print(text + str(number) + " is " + str(last) + " and is 0")
else:
    print(text + str(number) + " is " + str(last) + " and is less than 6 and not 0")
