#!/usr/bin/python3
"""Displays all values in the states table
where name matches the given argument"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    username, password, database, state_name = argv[1],\
        argv[2], argv[3], argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)
    cur = db.cursor()

    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (state_name,))
    query_results = cur.fetchall()

    for row in query_results:
        print(row)

    cur.close()
    db.close()
