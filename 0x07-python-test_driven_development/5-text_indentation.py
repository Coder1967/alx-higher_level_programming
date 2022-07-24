#!/usr/bin/python3
"module to print 2 new lines after either ?, ., or :"


def text_indentation(text):
    if type(text) != str:
        raise TypeError("text must be a string")
    " the 'checker' variable checks if we are cuurently on a new line"
    checker = 0

    for i in range(len(text)):
        if text[i] == '?' or text[i] == '.' or text[i] == ':':
            print('{}{}'.format(text[i], '\n\n'), end="")
            if text[i + 1] == ' ':
                checker = 1
        else:
            if checker == 1:
                checker = 0
                continue
            else:
                print(text[i], end="")
