#!/usr/bin/python3
"""
connecting with a database and making a simple query
using the database hbtn_0e_0_usa
"""
from sys import argv
import MySQLdb
if __name__ == '__main__':
    db = MySQLdb.connect(user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306, host='localhost')
    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE states.name LIKE %s
                ORDER BY states.id ASC;""", (argv[4],))
    results = cur.fetchall()
    for res in results:
        print(res)
    cur.close()
    db.close()
