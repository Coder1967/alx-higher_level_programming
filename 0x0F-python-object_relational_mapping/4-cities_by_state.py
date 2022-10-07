#!/usr/bin/python3
""" writing some basic sql query in python
by using the MySQLdb module
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1],
                         db=argv[3], port=3306, host='localhost')
    cur = db.cursor()
    cur.execute("""SELECT c.id, c.name, s.name from cities as c INNER
                    JOIN states as s on s.id=c.state_id ORDER BY c.id;""")
    results = cur.fetchall()
    for res in results:
        print(res)
    cur.close()
    db.close()
