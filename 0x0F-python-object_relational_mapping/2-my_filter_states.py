#!/usr/bin/python3
"""script that takes in an argument and displays all values"""
import MySQLdb
import sys

import MySQLdb

if __name__ == "__main__":
    import sys

    # Get the arguments from the command line
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL server
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
    )

    # Create a cursor
    cursor = connection.cursor()

    # Create the SQL query
    query = """
        SELECT *
        FROM states
        WHERE name = %s
        ORDER BY states.id ASC
    """

    # Execute the query
    cursor.execute(query, (state_name,))

    # Get the results
    results = cursor.fetchall()

    # Print the results
    for result in results:
        print(result)

    # Close the cursor and the connection
    cursor.close()
    connection.close()
