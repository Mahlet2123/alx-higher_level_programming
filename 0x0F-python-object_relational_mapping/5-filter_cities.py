#!/usr/bin/python3
"""
lists all cities from the database hbtn_0e_4_usa
code should not be executed when imported
"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3]
    )

    cur = db.cursor()

    argument = argv[4]

    cur.execute(
        """
        SELECT cities.name FROM cities
        LEFT JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
        """, (argument, )
    )
    rows = cur.fetchall()
    print(', '.join([row[0] for row in rows]))
    cur.close()
    db.close()
