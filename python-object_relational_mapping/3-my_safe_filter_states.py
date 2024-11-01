#!/usr/bin/python3
"""Script that takes in an argument and displays all
values in the states table of hbtn_0e_0_usa
where name matches the argument, with SQL injection protection."""

import MySQLdb
import sys

if __name__ == '__main__':
    """Connect to MySQL database using command-line arguments:
    user, password, database name"""
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()
    search_value = sys.argv[4]

    # Parameterized SQL query to prevent SQL injection
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (search_value,))

    # Fetch and display all query results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
