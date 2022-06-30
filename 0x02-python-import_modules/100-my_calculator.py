#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import mul, add, div, sub
    from sys import exit, argv

    length = len(argv) - 1

    if length != 3:
        print("<a> <operator> <b> = <result>")
        exit(1)
    my_dict = {"+": add, "/": div, "-": sub, "*": mul}
    a = int(argv[1])
    b = int(argv[3])

    if argv[2] not in list(my_dict):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{} {} {} = {}".format(a, argv[2], b, my_dict.get(argv[2])(a, b)))
    exit(1)
