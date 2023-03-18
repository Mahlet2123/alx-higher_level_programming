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
    cur.execute("SELECT * FROM cities ORDER BY cities.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
