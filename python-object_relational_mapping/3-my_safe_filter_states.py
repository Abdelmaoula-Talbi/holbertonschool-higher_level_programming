#!/usr/bin/python3
"""

A module that representes a script that takes in an argument and displays all
values in the states table of hbtn_0e_0_usa where name matches the argument

"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    name = argv[4]
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name=%(name)s\
            ORDER BY id ASC", {'name': name})
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
