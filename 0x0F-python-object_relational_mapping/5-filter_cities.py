#!/usr/bin/python3

#!/usr/bin/python3
"""
Lists all cities of a specific state from the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    Main execution block

    Args:
        username (_type_): MySQL username
        password (_type_): MySQL password
        database (_type_): MySQL database name
        state_name (_type_): Name of the state
    """

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    
    state_name = argv[4]
    cursor = db.cursor()
    query = """
            SELECT cities.name
            FROM cities
            INNER JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id ASC
            """
    cursor.execute(query, (state_name,))

    rows = cursor.fetchall()

    city_names = [row[0] for row in rows]
    print(', '.join(city_names))

    cursor.close()
    db.close()
