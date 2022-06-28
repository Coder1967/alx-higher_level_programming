#!/usr/bin/python3

def uppercase(str):
    num = 0

    for i in str:
        if ord(i) >= 97 and ord(i) <= 123:
            num += ord(i) - 32
            print(chr(num))
        else:
            print(i)
