#!/usr/bin/python3

"""
creation of new module
"""
import MySQLdb
# import sys
from sys import argv


if __name__ == "__main__":
    """
    declaring function

    Args:
        username (_type_): _description_
        password (_type_): _description_
        database (_type_): _description_
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
