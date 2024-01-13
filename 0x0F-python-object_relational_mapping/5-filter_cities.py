#!/usr/bin/python3
"""Queries cities TABLE and joins it with states
    and sorts by input"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    username, password, database, state_name = argv[1],\
        argv[2], argv[3], argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)
    cur = db.cursor()

    cur.execute("SELECT cities.name \
                 FROM cities \
                 INNER JOIN states \
                 ON cities.state_id = states.id \
                 WHERE states.name=%s \
                 ORDER BY cities.id ASC", (state_name, ))

    query_results = cur.fetchall()

    """Using list comprehension and join to generate
    comma separated strings"""
    city_names = [row[0] for row in query_results]
    result_str = ', '.join(city_names)
    print(result_str)

    cur.close()
    db.close()
