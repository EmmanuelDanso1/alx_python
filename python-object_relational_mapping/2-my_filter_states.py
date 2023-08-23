#!/usr/bin/python3
"""
a script that takes in an argument and displays all
values in the states table of hbtn_0e_0_usa
where name matches the argument
"""
import sys
import MySQLdb
def display_matching_states(username, password, db_name, state_name):
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
    query = "SELECT DISTINCT * FROM states WHERE LOWER(name) = LOWER('{}') ORDER BY id ASC".format(state_name)
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
    if len(sys.argv) != 5:
        print("Usage: python script.py <mysql_username> <mysql_password> <db_name> <state_name>")
    else:
        mysql_username = sys.argv[1]
        mysql_password = sys.argv[2]
        db_name = sys.argv[3]
        state_name = sys.argv[4]
        display_matching_states(mysql_username, mysql_password, db_name, state_name)
        