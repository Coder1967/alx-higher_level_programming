#!/usr/bin/python3
"""
connecting with a database and making a simple query
"""
if __name__ == '__main__':
    from sys import argv
    import  MySQLdb
    db = MySQLdb.connect(user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306, host='localhost')
    cur = db.cursor()
    cur.execute("""SELECT * FROM states ORDER BY states.id LIMIT 5""")
    results = cur.fetchall()
    for res in results:
        print(res)
    cur.close()
    db.close()
