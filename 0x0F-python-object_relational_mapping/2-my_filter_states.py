#!/usr/bin/python3

"""
creation of new module in ORM
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    state_name = argv[4]

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name = '{}' \
        ORDER BY id ASC".format(state_name)

    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
