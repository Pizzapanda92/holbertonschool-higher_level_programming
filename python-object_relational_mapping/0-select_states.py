#!/usr/bin/python3
"""cript that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == "__main__":

    """Connect to MySQL database using command-line arguments:
        user, password, database name"""

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create a cursor to execute queries
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all query results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
