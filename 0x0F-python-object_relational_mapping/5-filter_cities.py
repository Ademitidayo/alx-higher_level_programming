#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists all cities of that state,
using the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Command line arguments: username, password, database name, state name
    if len(sys.argv) != 5:
        print("Usage: {} username password database state_name".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    try:
        db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
    except MySQLdb.Error as e:
        print("Error connecting to MySQL database:", e)
        sys.exit(1)

    # Create a cursor object using cursor() method
    cursor = db.cursor()

    # SQL query to fetch cities of the specified state
    query = """
        SELECT GROUP_CONCAT(cities.name ORDER BY cities.id SEPARATOR ', ')
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
    """

    try:
        # Execute SQL query with safe parameterization
        cursor.execute(query, (state_name,))

        # Fetch the result
        result = cursor.fetchone()
        if result:
            print(result[0])

    except MySQLdb.Error as e:
        print("Error executing MySQL query:", e)
        sys.exit(1)

    finally:
        # Close cursor and database connection
        cursor.close()
        db.close()
