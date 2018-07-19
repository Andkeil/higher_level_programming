#!/usr/bin/python3
import MySQLdb
import sys
"""
Script list all states from database based on user input
safe from sql injection
"""


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name=%s",(sys.argv[4],))
    for row in cur:
        print("{}".format(row))
    cur.close()
    db.close()
