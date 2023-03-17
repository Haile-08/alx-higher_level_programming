#!/usr/bin/python3

"""
    a script that takes in an arguemnt and diaplays all
    values in the states table
"""


import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3307, user=argv[1],
                         password=argv[2], database=argv[3])
    cur= db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY\
                 '{}' ORDER BY id ASC".format(argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
