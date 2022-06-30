#!/usr/bin/python3

if __name__ == "__main__":

    from sys import argv

    i = 1
    sum = 0
    length = len(argv)

    while i < length:
        sum += int(argv[i])
        i += 1
    print(sum)
