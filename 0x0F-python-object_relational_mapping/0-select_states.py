#!/usr/bin/python3
"""
This script that lists all states from the database hbtn_0e_0_usa:
"""
import sys
import MySQLdb

"""
Variables With the Creditials.
"""
MY_HOST = "localhost"
MY_USER = sys.argv[1]
MY_PASS = sys.argv[2]
MY_DB = sys.argv[3]

if __name__ == "__main__":
    """
    MySQL Connection
    """
    db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
            )
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
