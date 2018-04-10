#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = number
if number < 0:
    number = number * -1
    ldig = number % 10
    ldig = ldig * -1
else:
    ldig = number % 10
if ldig > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".format(num, ldig))
elif ldig == 0:
    print("Last digit of {:d} is {:d} and is 0".format(num, ldig))
else:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0"
          .format(num, ldig))
