#!/usr/bin/python3
"""
connecting with a database and making a simple query
"""
from sys import argv
import MySQLdb
if __name__ == '__main__':
    db = MySQLdb.connect(user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306, host='localhost')
    cur = db.cursor()
    cur.execute("""SELECT * FROM states ORDER BY states.id ASC;""")
    results = cur.fetchmany(5)
    for res in results:
        print(res)
    cur.close()
    db.close()
