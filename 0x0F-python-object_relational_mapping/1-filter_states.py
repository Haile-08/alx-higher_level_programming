#!/usr/bin/python3

"""
    A script  that lists all states with a name starting with N
    form (upper N) from the database hbtn_0e_0_usa
"""


import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], password=argv[2],
                         database=argv[3], host='localhost', port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name\
                 LIKE BINARY 'N%' ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
