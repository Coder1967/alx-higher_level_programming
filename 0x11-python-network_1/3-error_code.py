#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8).
or the error code in the case of a failure
"""
if __name__ == '__main__':
    from urllib import request
    from urllib import error
    from sys import argv
    try:
        url = request.Request(argv[1])
        with request.urlopen(url) as resp:
            result = resp.read()
            print(result.decode('utf-8'))
    except error.HTTPError as e:
        print('Error code: {}'.format(e.code))
