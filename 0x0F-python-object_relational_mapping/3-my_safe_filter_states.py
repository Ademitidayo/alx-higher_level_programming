#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL username, password, database name, and state name from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4]

    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=dbname, port=3306)
        # Create a cursor object to interact with the database
        cursor = db.cursor()

        # Prepare a parameterized query to avoid SQL injection
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

        # Execute the SQL query with the state_name as the parameter
        cursor.execute(query, (state_name,))

        # Fetch all the rows from the executed query
        rows = cursor.fetchall()

        # Loop through the rows and print each one
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print(f"Error {e}")

    finally:
        # Close the cursor and the connection if they exist
        if cursor:
            cursor.close()
        if db:
            db.close()
