#!/usr/bin/python3
""" script to fetch url address:https://alx-intranet.hbtn.io/status"""


from urllib.request import urlopen
if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    with urlopen(url) as resp:
        cont = resp.read()
        print('Body response:')
        print('\t- type: {}'.format(type(cont)))
        print('\t- content: {}'.format(cont))
        print('\t- utf8 content: {}'.format(cont.decode('utf-8')))
