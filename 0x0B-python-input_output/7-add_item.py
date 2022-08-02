#!/usr/bin/python3
"""
script appends items to a list in
the add_item.json file
"""


if __name__ == "__main__":
    save = __import__("5-save_to_json_file").save_to_json_file
    load = __import__("6-load_from_json_file").load_from_json_file
    from sys import argv

    try:
        obj = load("add_item.json")

    except FileNotFoundError:
        obj = []
        save(obj, "add_item.json")
        exit(0)
    i = 1

    while i < len(argv):
        obj.append(argv[i])
        i += 1
    save(obj, "add_item.json")
