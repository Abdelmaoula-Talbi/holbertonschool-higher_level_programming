#!/usr/bin/python3
"""

A module that representes a script that lists all states from
the database hbtn_0e_0_usa

"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    State_Name = argv[4]
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities JOIN states ON states.id = cities.state_id WHERE states.name = %(State_Name)s ORDER BY cities.id", {'State_Name': State_Name})
    rows = cur.fetchall()
    for row in rows:
     print(", ".join(row))
    cur.close()
    db.close()
