#!/usr/bin/python3
"""
 script that takes in a letter and sends a POST request to
 http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
if __name__ == '__main__':
    import requests
    from sys import argv
    from sys import argv
    if len(argv) == 2:
        q = argv[1]
    else:
        q = ""
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        new_dict = r.json()
        id = new_dict.get('id')
        name = new_dict.get('name')
        if len(new_dict) == 0 or not id or not name:
            print("No result")
        else:
            print("[{}] {}".format(new_dict['id'], new_dict['name']))
    except KeyError:
        print("Not a valid JSON")
