#!/usr/bin/python3
import MySQLdb
import sys
"""
Script list all states from database
"""


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    for row in cur:
        print("{}".format(row))
    cur.close()
    db.close()
