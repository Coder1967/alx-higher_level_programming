#!/usr/bin/python3

def print_last_digit(number):
    num = 0

    if number < 0:
        num = number * -1
        num %= 10
    else:
        num = number % 10

    print("{:d}".format(num), end="")
    return (num)
