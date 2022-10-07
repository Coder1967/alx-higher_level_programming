#!/usr/bin/python3
"""
connecting with a database and making a simple query
using the database hbtn_0e_0_usa
"""
if __name__ == '__main__':
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306, host='localhost')
    cur = db.cursor()
    cur.execute('SELECT * FROM states WHERE name LIKE "N%" ORDER BY id;')
    results = cur.fetchall()
    for res in results:
        print(res)
    cur.close()
    db.close()
