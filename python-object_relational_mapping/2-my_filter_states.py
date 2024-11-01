#!/usr/bin/python3
# script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument
import MySQLdb
import sys

if __name__ == '__main__':

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()
    # Get the search value from the command-line argument
    search_value = sys.argv[4]

    # Execute SQL query to select states where the name matches the search value
    cursor.execute(
        "SELECT * from states WHERE name = %s ORDER BY id ASC", (search_value,))

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
