#!/usr/bin/python3

for i in range(1, 90):
    if int(str(i % 10) + str(int(i / 10))) > i:
        if i != 89:
            print("{:02d}".format(i), end=", ")
        else:
            print("{:02d}".format(i))
