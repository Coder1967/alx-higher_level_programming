#!/usr/bin/python3
"""
takes argument from the cndline
and prints the value of the header
'X-Request-Id' to the terminal
"""
from urllib.request import urlopen
from sys import argv
if __name__ == '__main__':
    url = argv[1]
    with urlopen(url) as resp:
        print(resp.headers['X-Request-Id'])
