#!/usr/bin/python3
"""
a script displays all cities
values in the states table of hbtn_0e_0_usa
"""
import sys
import MySQLdb
def list_cities(username, password, db_name):
    # Establishing a connection to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )
    """
    Creating a cursor object to
    interact with the database

    """
    cursor = db.cursor()
    """
    Creating and executing
    the SQL query using user input
    """
    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC
    """
    cursor.execute(query)
    # Fetch all matching rows
    rows = cursor.fetchall()
    # Display the results
    for row in rows:
        print(row)
    # Close the cursor and connection
    cursor.close()
    db.close()
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py mysql_user mysql_password db_name")
    else:
        mysql_username = sys.argv[1]
        mysql_password = sys.argv[2]
        db_name = sys.argv[3]
        list_cities(mysql_username, mysql_password, db_name)
