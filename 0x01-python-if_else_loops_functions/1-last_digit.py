#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

num = 0

if number < 0:
    num += -1 * number
    num = -1 * (num % 10)

elif number >= 0:
    num += number % 10

if num > 5:
    print(f"Last digit of {number} is {num} and is greater than 5")
elif num == 0:
    print("Last digit of {} is {} and is 0".format(number, num))
elif num < 6 and num != 0:
    print("Last digit of {} is {} and is less than 6\
 and not 0".format(number, num))
