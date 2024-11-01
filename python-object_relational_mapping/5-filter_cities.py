#!/usr/bin/python3
"""
This script takes in the name of a state as an argument and lists all cities
of that state from the database 'hbtn_0e_4_usa'. The results are displayed
as a comma-separated list of city names, sorted in ascending order by city ID.
"""
import MySQLdb
import sys


if __name__ == "__main__":

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()
    search_value = sys.argv[4]
    command = ("""
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """)
    cursor.execute(command, (search_value,))

    rows = cursor.fetchall()
    city_names = ", ".join([row[0] for row in rows])
    print(city_names)

    cursor.close()
    db.close()
