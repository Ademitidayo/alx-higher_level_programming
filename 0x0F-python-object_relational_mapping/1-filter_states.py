#!/usr/bin/python3
"""
Script that lists all states with a name starting with 
N from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Command line arguments: username, password, database name
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

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

    # Query to select states starting with 'N', ordered by id
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id"

    try:
        # Execute SQL query
        cursor.execute(query)

        # Fetch all the rows and print them
        results = cursor.fetchall()
        for row in results:
            print(row)

    except MySQLdb.Error as e:
        print("Error executing MySQL query:", e)
        sys.exit(1)

    finally:
        # Close cursor and database connection
        cursor.close()
        db.close()
