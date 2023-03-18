#!/usr/bin/python3
"""
List states Module from the database hbtn_0e_0_usa
where name matches the argument.
"""


import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3]
    )
    cur = db.cursor()

    argument = argv[4]

    cur.execute(
        """SELECT * FROM states WHERE states.name LIKE BINARY '{}' ORDER BY \
states.id ASC""".format(argv[4])
    )
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
