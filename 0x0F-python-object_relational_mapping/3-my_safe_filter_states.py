#!/usr/bin/python3
"""
module created
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    """_summary_

    Args:
        username (_type_): _description_
        password (_type_): _description_
        database (_type_): _description_
        state_name (_type_): _description_
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    cursor.execute(query, (state_name,))

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
