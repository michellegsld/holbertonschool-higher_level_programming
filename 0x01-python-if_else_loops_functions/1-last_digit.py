#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of {:d} is ".format(number), end = '')
if number < 0 and number % 10 != 0:
    print("-", end = '')
print("{:d} ".format(abs(number) % 10), end = '')
if abs(number) % 10 > 5 and number > 0:
    print("and is greater than 5")
elif number % 10 == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
