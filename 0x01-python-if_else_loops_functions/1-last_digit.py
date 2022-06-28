#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

num = int(number % 10)
if num < 0:
    num *= -1
if num > 5:
    print(f"Last digit of {number} is {num} and is greater than 5")
elif num == 0:
    print("Last digit of {} is {} and is 0".format(number, num))
elif num < 6 and num != 0:
    print("Last digit of {} is {} and is less than 6\
 and not 0".format(number, num))
