#!/usr/bin/python3
"""

A module that representes a script that lists all states from
the database hbtn_0e_0_usa

"""

if __name__ == "__main__":
    import MySQLdb
    db = MySQLdb.connect(host="localhost", port=3306, user="My_User", passwd="My_Passwd", db="hbtn_0e_0_usa")
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
