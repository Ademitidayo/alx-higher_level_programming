#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL username, password, and database name from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    try:
        # Connect to the MySQL server
        conn = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=dbname, charset="utf8")
        cursor = conn.cursor()

        # Execute the SQL query to select all states, ordered by id
        cursor.execute("SELECT * FROM states ORDER BY id ASC")

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
        if conn:
            conn.close()
