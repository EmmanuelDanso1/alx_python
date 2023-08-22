"""
This is an object relational mapping project with
MySQL and Python
A script that lists all states with a name
starting with N (upper N) from the database hbtn_0e_0_usa
"""
import MySQLdb  # Import the MySQLdb module for MySQL database interaction
import sys      # Import the sys module for system-related functionality


def list_states_starting_with_N(mysql_user, mysql_password, db_name):
        # using try and except handlers to catch errors
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_user,
            passwd=mysql_password,
            db=db_name)
        # Create a cursor object to interact
        cur = db.cursor()
        # Construct the SQL query to retrieve states sorted by N&ID
        q = (
            "SELECT * FROM states"
            "WHERE BINARY name LIKE 'N%'"
            "ORDER BY states.id ASC")
        # Execute the query
        cur.execute(q)
        # Fetching all the rows returned by the query
        rows = cur.fetchall()
        # Display the results
        for row in rows:
            print(row)
        # Close the cursor and database connection
        cur.close()
        db.close()
    except MySQLdb.Error as e:
        # print error if any and exit
        print("MySQL Error:", e)
        sys.exit(1)
if __name__ == "__main__":
    # Check if the correct number of command-line
    #  arguments is provided
    if len(sys.argv) != 4:
        print("Usage: python script.py mysql_user mysql_password db_name")
        sys.exit(1)
    # Getting uname,pswd and db from commandline
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    # Caling the list function
    list_states_starting_with_N(mysql_user, mysql_password, db_name)
