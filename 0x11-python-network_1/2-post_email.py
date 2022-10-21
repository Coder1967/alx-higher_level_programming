#!/usr/bin/python3
"""
script that takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays
the body of the response (decoded in utf-8)
"""
from sys import argv
import urllib
if __name__ == '__main__':
    params = {email: argv[2]}
    data = urllib.parse.urlencode(params)
    data = data.encode('ascii')
    url = urllib.request.Request(argv[1], data)
    with urllib.request.urlopen(url) as res:
        print(res.read().decode('utf-8'))
