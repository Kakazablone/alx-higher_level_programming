#!/usr/bin/python3
"""This module runs a query on MySQ retrieve
all records from the 'states' table"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    username, password, database = argv[1], argv[2], argv[3]

    """Establish a connection to the MySQL database"""
    try:
        db_conn = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=database
        )
    except MySQLdb.Error as err:
        print("Error: {}".format(err))
        exit(1)

    cur = db_conn.cursor()

    """Execute the SQL query to retrieve all records from the 'states' table"""
    try:
        cur.execute("SELECT * FROM states ORDER BY id ASC")
        query_db = cur.fetchall()
    except MySQLdb.Error as err:
        print("Error executing query: {}".format(err))
        cur.close()
        db_conn.close()
        exit(1)

    for row in query_db:
        print(row)

    cur.close()
    db_conn.close()
