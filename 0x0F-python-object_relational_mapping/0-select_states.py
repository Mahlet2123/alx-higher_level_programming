#!/usr/bin/python3
"""List states Module from the database hbtn_0e_0_usa
	Your script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)
	You must use the module MySQLdb (import MySQLdb)
	Your script should connect to a MySQL server running on localhost at port 3306
	Results must be sorted in ascending order by states.id
	Results must be displayed as they are in the example below
	Your code should not be executed when imported
"""


import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3]
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM hbtn_0e_0_usa.states ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
