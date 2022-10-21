#!/usr/bin/python3
"""
script prints out the last ten commits
made by a user on a particular repo
"""
if __name__ == '__main__':
    from sys import argv
    import requests
    url = "https://api.github.com/repos/{}/{}/commits".format(
            argv[2], argv[1])
    r = requests.get(url)
    comm = r.json()
    try:
        for i in range(0, 10):
            print("{}: {}".format(
                comm[i]["sha"],
                comm[i]["commit"]["author"]["name"]))
    except IndexError:
        pass
