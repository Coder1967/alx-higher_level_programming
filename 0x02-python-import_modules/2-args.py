#!/usr/bin/python3

from sys import argv

l = len(argv) - 1
i = 1

if l == 0:
    print("0 arguments.")
elif l == 1:
    print("1 argument:")
    print("{}: {}".format(l, argv[1]))
else:
    print("{} arguments:".format(l))
    while i <= l:
        print("{}: {}".format(i, argv[i]))
        i += 1
