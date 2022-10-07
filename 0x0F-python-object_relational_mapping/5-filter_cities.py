#!/usr/bin/python3
""" writing some basic sql query in python
by using the MySQLdb module
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    res = ""
    i = 0

    db = MySQLdb.connect(user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306, host='localhost')
    cur = db.cursor()
    cur.execute("""SELECT cities.name FROM cities WHERE
                state_id = (SELECT id from states WHERE name=%s);""", (argv[4],))
    results = cur.fetchall()
    while i < len(results):
        res += results[i][0];
        if (i != len(results) - 1):
                res += ', '
        i += 1;
    print(res)
    cur.close()
    db.close()
