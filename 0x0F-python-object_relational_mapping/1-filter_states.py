#!/usr/bin/python3
"""
New module creation
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    """_summary_

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

    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
