#!/usr/bin/python3

"""
import random
number = random.randint(-10000, 10000)
To get the last digit of a number, use
the modulos operator
last_digit = abs(number) % 10
print("Last digit of", number, "is", last_digit, end=" ")
if (last_digit > 5):
    print("and is greater than 5")
elif (last_digit == 0):
    print("and is 0")
elif (last_digit < 6 and not 0):
    print("and is less than 6 and not 0")

"""

import random

number = random.randint(-10000, 10000)
last_digit = abs(number) % 10

number = "Last digit of {} is {}".format(number, last_digit)
if last_digit > 5:
    number += " and is greater than 5"
elif last_digit == 0:
    number += " and is 0"
else:
    number += " and is less than 6 and not 0"

print(number)