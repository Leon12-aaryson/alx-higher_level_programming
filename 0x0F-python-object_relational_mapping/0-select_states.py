#!/usr/bin/python3

"""
creation of new module
"""
import MySQLdb
from sys import argv


def list_states(username, password, database):
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


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    username, password, database = sys.argv[1:4]

    list_states(username, password, database)
