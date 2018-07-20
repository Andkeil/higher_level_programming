#!/usr/bin/python3
import MySQLdb
import sys
"""
Script list all cities from database from user input state
"""


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM cities JOIN states ON\
    cities.state_id = states.id WHERE states.name =%s\
    ORDER BY cities.id ASC", (sys.argv[4],))
    results = cur.fetchall()
    arr = []
    for row in results:
        if row[4] == sys.argv[4]:
            arr.append(row[2])
    print(", ".join(arr))
    cur.close()
    db.close()
