#!/usr/bin/python3
"""Lists all states with a name starting
with N from the database hbtn_0e_0_usa"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    username, password, database = argv[1], argv[2], argv[3]

    """Establish a connection to the MySQL database"""
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)
    cur = db.cursor()

    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cur.execute(query)
    query_results = cur.fetchall()

    for row in query_results:
        if (row[1][0] == 'N'):
            print(row)

    cur.close()
    db.close()
